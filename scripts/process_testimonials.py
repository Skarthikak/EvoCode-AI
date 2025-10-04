import requests
import json
import os

class TestimonialProcessor:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
    def get_testimonials(self):
        url = f"https://api.github.com/repos/{os.getenv('GITHUB_REPOSITORY')}/issues"
        params = {'labels': 'testimonial', 'state': 'all'}
        
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
    
    def generate_testimonial_display(self):
        testimonials = self.get_testimonials()
        
        html = '<div class="testimonials-grid">\n'
        
        for testimonial in testimonials[:5]:
            html += f'''
            <div class="testimonial-card">
                <h4>{testimonial["title"].replace("[TESTIMONIAL] ", "")}</h4>
                <p>{testimonial["body"][:150]}...</p>
                <div class="testimonial-meta">
                    <strong>By: {testimonial["user"]["login"]}</strong>
                </div>
            </div>
            '''
        
        html += '</div>'
        
        with open('docs/testimonials.html', 'w') as f:
            f.write(html)
        
        return html

if __name__ == "__main__":
    processor = TestimonialProcessor()
    processor.generate_testimonial_display()
    print("Testimonials processed!")
