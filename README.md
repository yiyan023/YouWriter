# YouWriter 🚀

## Inspiration ✨
The time-consuming process of watching videos and taking notes can discourage students from retaining knowledge and staying engaged. By creating a notes, bullet point, or essay summary from any YouTube link, YouWrite is an efficient way for students to grasp knowledge from videos.

## What does this app do? ⁉️
YouWriter converts YouTube videos into short summarizes in hopes of increasing note-taking efficiency for students of all demographics.

## How does it work? 👩‍💻
- The user is initially directed to a login page, where the user must input an existing username & password. If it is not an existing user, they must create a new account before gaining access to YouWriter. Their personal information is stored within a data storage system to ensure secure user authentication flow using Python, Flask, and MongoDB.
- When the user is redirected to the landing page, they are given the option to input a YouTube URL, start & end timestamps and to select their form of summary (see picture below). This responsive user interface was created using React and Tailwind CSS.
  
![image](https://github.com/yiyan023/YouWriter/assets/56096857/a34bda7d-ddd9-438b-ae68-f75e76087ba2)

- After the user inputs all their parameters & clicks submit, the video transcript is extracted and converted into a summarized JSON file using Python, Flask, OpenAI. It is then sent back to the client-side where the user can retrieve the summary of this YouTube video.
