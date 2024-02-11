import React, { createContext, useState, useContext } from "react";

const SummaryContext = createContext();

export const useSummary = () => useContext(SummaryContext);

export const SummaryProvider = ({ children }) => {
    const [summary, setSummary] = useState(null);

    return (
        <SummaryContext.Provider value={{ summary, setSummary }}>
            {children}
        </SummaryContext.Provider>
    );
};
