import React from "react";
import { BrowserRouter } from "react-router-dom";

import { About, Home, Navbar, Notes, Summarize, Summary } from "./components";
import { SummaryProvider } from "./contexts/SummaryContext";

const App = () => {
    return (
        <BrowserRouter>
            <div className="relative z-0 bg-white">
                {/* <Home /> */}
                <Navbar />
                <SummaryProvider>
                    <Summarize />
                    <Summary />
                </SummaryProvider>
                {/* <About /> */}
            </div>
        </BrowserRouter>
    );
};

export default App;
