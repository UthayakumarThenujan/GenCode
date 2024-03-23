import React, { useState, useRef, useEffect } from "react";
import axios from 'axios'; // Import Axios
import './TopicForm.css';

const TopicForm = () => {
    const [topic, setTopic] = useState('');
    const [apiResponses, setApiResponses] = useState([]);
    const apiDataRef = useRef(null);

    const handleGenerate = () => {
        // Send a POST request to the API endpoint with the topic data
        axios.post('http://127.0.0.1:8000/topic', { "Topic":topic })
            .then(response => {
                // Handle the response
                setApiResponses(prevResponses => [...prevResponses, response.data]);
            })
            .catch(error => {
                // Handle errors
                console.error('Error posting data:', error);
            });
    };

    const scrollToBottom = () => {
        // Scroll to the last response
        apiDataRef.current.scrollIntoView({ behavior: 'smooth', block: 'end' });
    };

    useEffect(() => {
        // Scroll to the last response when apiResponses change
        scrollToBottom();
    }, [apiResponses]);

    return (
        <div>
            {apiResponses.map((response, index) => (
                <div key={index} className="api-data">
                    {/* Box with text */}
                    <div className="box-with-text">Response {index + 1}</div>
                    {/* Display API response */}
                    <div dangerouslySetInnerHTML={{ __html: response }} />
                </div>
            ))}
            {apiResponses.length > 2 && (
                <button className="scroll-to-bottom-button" onClick={scrollToBottom}>
                    Scroll to Last Response
                </button>
            )}
            <div ref={apiDataRef} /> {/* Empty div for scrolling to the last response */}
            <div className="chat-wrapper">
                <div className="chat-input">
                    <input
                        type="text"
                        placeholder="Message to GenCode..."
                        value={topic}
                        onChange={(event) => setTopic(event.target.value)}
                        required
                    />
                </div>
                <div className="generate-button">
                    <button type="button" onClick={handleGenerate}>Generate</button>
                </div>
            </div>
        </div>
    );
};

export default TopicForm;
