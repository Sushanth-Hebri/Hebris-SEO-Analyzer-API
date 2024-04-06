
# Hebris SEO Analyzer API
An Open ended API , that analyzes SEO performance and returns score and checkings

## Overview

Hebris SEO Analyzer is a RESTful API designed to analyze the Search Engine Optimization (SEO) metrics of a given URL. It provides insights into various SEO factors such as meta tags, content optimization, accessibility, mobile-friendliness, and more. The API calculates weighted scores for each SEO factor, suggests improvements based on missing elements, and generates an overall SEO score for the analyzed webpage.

## Endpoint

The API endpoint for Hebris SEO Analyzer is: https://hebris-seo.onrender.com?url=


## Features

- Analyze SEO elements status including Meta Title, Meta Description, Meta Keywords, H1 Tags, Total Links, Image Alt Tags, etc.
- Calculate weighted scores for each SEO factor based on their importance.
- Generate suggestions to improve SEO based on missing elements.
- Determine the overall SEO score of the webpage.

## Getting Started

To use the API, simply make a GET request to the endpoint with the URL parameter:

https://hebris-seo.onrender.com?url=<URL_TO_ANALYZE>

Replace `<URL_TO_ANALYZE>` with the URL you want to analyze.

### Example Request

http
GET /?url=https://www.example.com HTTP/1.1
Host: hebris-seo.onrender.com

 ### Response example
{
    "SEO Elements Status": {
        "Meta Title": "Present",
        "Meta Description": "Missing",
        "Meta Keywords": "Missing",
        "H1 Tags": "Missing",
        "Total Links": 5,
        "Image Alt Tags": 17,
        "Secure and Accessible Website": "Yes",
        "Mobile Friendly": "No",
        "Outbound Links Count": 0,
        "Internal Links Count": 0,
        "Access Time (s)": 1.2738912105560303
    },
    "Weighted Scores": {
        "Meta Title": 100,
        "Meta Description": 0,
        "Meta Keywords": 0,
        "H1 Tags": 0,
        "Total Links": 0,
        "Image Alt Tags": 0,
        "Secure and Accessible Website": 0,
        "Mobile Friendly": 0,
        "Outbound Links Count": 0,
        "Internal Links Count": 0,
        "Access Time (s)": 0
    },
    "Suggestions": {
        "Meta Title": "Optimize content for better SEO",
        "Meta Description": "Add appropriate content",
        "Meta Keywords": "Add appropriate content",
        "H1 Tags": "Add appropriate content"
    },
    "SEO Score": 100
}





