from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from bs4 import BeautifulSoup
import time
import re
import json

# Define weights for SEO factors based on their contribution to search rankings
SEO_WEIGHTS = {
    'Meta Title': 10,
    'Meta Description': 10,
    'Meta Keywords': 10,
    'H1 Tags': 5,
    'Total Links': 5,
    'Image Alt Tags': 5,
    'Secure and Accessible Website': 10,
    'Mobile Friendly': 10,
    'Outbound Links Count': 5,
    'Internal Links Count': 5,
    'Access Time (s)': 5  # Adjust weight based on importance
}

class SEORequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.send_header('Access-Control-Allow-Methods', 'GET')  # Allow only GET requests
        self.end_headers()

        url = self.path.lstrip('/?url=')
        if not url:
            response_data = {'error': 'Missing URL parameter'}
            self.wfile.write(json.dumps(response_data).encode())
            return

        # Fetch HTML content and measure access time
        html_content, access_time = self.fetch_html(url)

        # Analyze SEO metrics and get status, weighted scores, and overall score
        seo_elements_status, weighted_scores, seo_score = self.analyze_seo(html_content, access_time, url)

        # Prepare JSON response
        response_data = {
            'SEO Elements Status': seo_elements_status,
            'Weighted Scores': weighted_scores,
            'SEO Score': seo_score
        }

        self.wfile.write(json.dumps(response_data).encode())

    def fetch_html(self, url):
        try:
            start_time = time.time()  # Start measuring access time
            response = requests.get(url)
            end_time = time.time()  # Stop measuring access time
            access_time = end_time - start_time  # Calculate access time

            if response.status_code == 200:
                return response.text, access_time  # Return HTML content and access time
            else:
                return None, access_time
        except Exception as e:
            print(f"Error fetching HTML: {e}")
            return None, None  # Return None for both content and access time in case of an error

    def analyze_seo(self, html_content, access_time, url):
        if not html_content:
            return "Error: No HTML content to analyze", {}, 0

        soup = BeautifulSoup(html_content, 'html.parser')

        # Example SEO metrics to analyze
        meta_title = soup.find('title')
        meta_description = soup.find('meta', attrs={'name': 'description'})
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        h1_tags = soup.find_all('h1')
        total_links = len(soup.find_all('a'))
        image_alt_tags = soup.find_all('img', alt=True)
        secure_website = 'https' in url
        mobile_friendly = self.is_mobile_friendly(html_content)
        outbound_links_count = self.get_outbound_links_count(html_content, url)
        internal_links_count = self.get_internal_links_count(html_content, url)

        # Initialize a dictionary to store SEO elements status
        seo_elements_status = {
            'Meta Title': 'Present' if meta_title else 'Missing',
            'Meta Description': 'Present' if meta_description else 'Missing',
            'Meta Keywords': 'Present' if meta_keywords else 'Missing',
            'H1 Tags': 'Present' if len(h1_tags) > 0 else 'Missing',
            'Total Links': total_links,
            'Image Alt Tags': len(image_alt_tags),
            'Secure and Accessible Website': 'Yes' if secure_website else 'No',
            'Mobile Friendly': 'Yes' if mobile_friendly else 'No',
            'Outbound Links Count': outbound_links_count,
            'Internal Links Count': internal_links_count,
            'Access Time (s)': access_time  # Include access time in the SEO elements status
        }

        # Calculate weighted scores for each SEO factor
        weighted_scores = {factor: (SEO_WEIGHTS[factor] * 10 if status == 'Present' else 0) for factor, status in seo_elements_status.items()}

        # Calculate overall SEO score based on weighted scores
        seo_score = sum(weighted_scores.values())

        return seo_elements_status, weighted_scores, seo_score

    def is_mobile_friendly(self, html_content):
        # Check for mobile-friendly content based on HTML/CSS structure
        mobile_friendly_classes = ['mobile', 'tablet', 'responsive', 'adaptive']
        for cls in mobile_friendly_classes:
            if cls in html_content.lower():
                return True
        return False

    def get_outbound_links_count(self, html_content, url):
        # Example: Count outbound links in the HTML content
        # This is a placeholder function for demonstration purposes
        return len(re.findall(r'<a .*?href="http[s]?://(?!' + url + ')[^"]+".*?>', html_content))

    def get_internal_links_count(self, html_content, url):
        # Example: Count internal links in the HTML content
        # This is a placeholder function for demonstration purposes
        return len(re.findall(r'<a .*?href="http[s]?://' + url + '[^"]+".*?>', html_content))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SEORequestHandler)
    print('Starting SEO analysis server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
