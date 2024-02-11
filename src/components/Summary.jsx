import React from "react";

import { useSummary } from "../contexts";

const Summary = () => {
    const { summary } = useSummary();

    return (
        <>
            {summary && (
                <div class="w-full bg-[#E0E7FF]" id="summary">
                    <div class="w-[55vw] items-center mx-auto min-h-screen p-4">
                        <h2 class="text-[32px] font-semibold pt-20 my-2">
                            Summary:
                        </h2>
                        <a href={summary.url} target="_blank" rel="noreferrer">
                            <h3 class="text-[20px] font-semibold hover:underline">
                                Video: {summary.title}
                            </h3>
                        </a>
                        <div className="mt-4 rounded-2xl">
                            {summary.type === "point-form" ? (
                                <ul class="list-disc ml-5">
                                    {summary.text.map((point) => (
                                        <li>{point}</li>
                                    ))}
                                </ul>
                            ) : (
                                summary.text
                            )}
                        </div>
                    </div>
                </div>
            )}
        </>
    );
};

export default Summary;
