import os
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
from pytube import YouTube

from . import openAI_client


class Summarizer:
    # test parameters (replace with user input later)
    # url = 'https://www.youtube.com/watch?v=NJZ5YNrXMpE&ab_channel=oliSUNvia'
    # # url = 'https://www.youtube.com/watch?v=h6fcK_fRYaI&ab_channel=Kurzgesagt%E2%80%93InaNutshell'
    # wordCount = 100
    # startTime = 0
    # endTime = 0

    # split transcript up into 10000-character chunks
    @staticmethod
    def chunk_transcript(transcript, chunk_size=10000):
        chunks = [transcript[i:i+chunk_size]
                  for i in range(0, len(transcript), chunk_size)]
        return chunks

    # get transcript from youtube

    @staticmethod
    def getTranscriptText(transcriptjson, startTime, endTime):
        transcript = ''

        result = []

        for item in transcriptjson:
            if int(item['start']) in range(startTime, endTime):
                result.append(item)

        for item in result:
            clip = item['text']
            transcript += f' {clip}'

        return transcript

    # get summary of transcript using openai (wordcount specified by user)
    @staticmethod
    def getSummary(transcript_chunks, wordCount, summary_type):
        summary = ""

        # commands for openai
        conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "assistant", "content": f"Write a {wordCount} word {summary_type} summary of this video."}]

        # run it on every chunk of transcript
        for chunk in transcript_chunks:
            conversation.append({"role": "user", "content": chunk})
            response = openAI_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation
            )
            summary += f" {response.choices[0].message.content}"

            # Clear user input for the next chunk
            conversation = conversation[:-1]

        return summary

    @staticmethod
    def getEndtime(transcriptjson):
        return transcriptjson[-1]['start']

    # keep on passing through ai until reaches specified wordcount
    @staticmethod
    def getFinalsummary(url, wordCount, startTime=0, endTime=None, summary_type="paragraph"):

        video_id = url.replace('https://www.youtube.com/watch?v=', '')
        transcriptjson = YouTubeTranscriptApi.get_transcript(
            video_id, languages=['en', "en-GB"])

        if endTime == None:
            Summarizer.getEndtime(transcriptjson)

        transcriptText = Summarizer.getTranscriptText(
            transcriptjson, startTime, endTime)

        # every word has ~6.5 characters on average
        while len(transcriptText) > wordCount*6.5:
            transcript_chunks = Summarizer.chunk_transcript(transcriptText)
            transcriptText = Summarizer.getSummary(
                transcript_chunks, wordCount, summary_type)

        # output to user interface
        return transcriptText

        # pprint.pprint(transcriptjson)
        # print(YouTubeTranscriptApi.list_transcripts(video_id))

    @staticmethod
    def timestamp_to_seconds(timestamp):
        timestamp = [int(x) for x in timestamp.split(':')]
        timestamp.reverse()

        seconds = sum([timestamp[i] * 60**i for i in range(len(timestamp))])

        return seconds

    @staticmethod
    def generate_pointform(input_text):
        conversation = f"Make point form notes of following text:\n{input_text}\nSummary:"
        response = openAI_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        summary = response['choices'][0]['text'].strip()
        return summary

    @staticmethod
    def get_video_title(url):
        try:
            video = YouTube(url)
            return video.title
        except Exception as e:
            return f"An error occurred: {e}"

# print(len(YouTubeTranscriptApi.get_transcript("NJZ5YNrXMpE&ab_channel=oliSUNvia", languages=['en', "en-GB"])))
# print(Summarizer.getFinalsummary('https://www.youtube.com/watch?v=NJZ5YNrXMpE&ab_channel=oliSUNvia', 100, 1700, 3000))
