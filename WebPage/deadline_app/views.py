"""
Views for the Deadline App

This module contains the API views for our "Why Developers Work on Deadline" webpage.
It provides both the main page view and the API endpoint that serves data to the frontend.
"""

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HomePageView(APIView):
    """
    API view that serves our homepage
    
    This view renders the main index.html template which contains our
    humorous webpage about why developers work on deadlines.
    """
    def get(self, request):
        """Handle GET requests by rendering the index template"""
        return render(request, 'index.html')

class DeadlineDataView(APIView):
    """
    API view that returns data about developer deadlines
    
    This view provides the JSON data that populates our webpage's
    dynamic content sections including the timeline, science facts,
    survival kit items, and quotes.
    """
    def get(self, request):
        """
        Handle GET requests by returning structured data about developer deadlines
        
        Returns:
            Response: JSON response containing all the data needed for the webpage
        """
        # Data structure containing all the content for our webpage
        data = {
            # Timeline stages showing the developer's journey through a project
            'timeline_stages': [
                {
                    'day': 1,
                    'title': "We've Got Time",
                    'description': "Project assigned. Developer calculates they have 336 hours until deadline.",
                    'progress': 0,
                    'thought': "I'll start tomorrow after I finish watching this tutorial series on a programming language I'll never use."
                },
                {
                    'day': 7,
                    'title': "Still Plenty of Time",
                    'description': "Developer spends day reorganizing desk and optimizing development environment.",
                    'progress': 5,
                    'thought': "I can't possibly work efficiently with these unaligned desktop icons."
                },
                {
                    'day': 10,
                    'title': "Starting to Code",
                    'description': "Developer creates project structure and writes first few lines of code.",
                    'progress': 10,
                    'thought': "Let me just refactor this perfectly working code for the third time."
                },
                {
                    'day': 13,
                    'title': "Mild Concern",
                    'description': "First realization that deadline is approaching. Decides to 'work on it over the weekend.'",
                    'progress': 15,
                    'thought': "I work better under pressure anyway."
                },
                {
                    'day': 14,
                    'title': "Panic Mode Activated",
                    'description': "Suddenly, developer achieves superhuman coding abilities.",
                    'progress': 100,
                    'thought': "I AM ONE WITH THE CODE. THE CODE IS WITH ME."
                }
            ],
            
            # Scientific explanations for the deadline phenomenon
            'science_facts': [
                {
                    'title': "Parkinson's Law",
                    'description': "Work expands to fill the time available for its completion.",
                    'explanation': "Translation: If you have two weeks, you'll take two weeks. If you have 24 hours, you'll do it in 24 hours."
                },
                {
                    'title': "Adrenaline Coding",
                    'description': "The body's fight-or-flight response kicks in, flooding the brain with chemicals that enhance focus and performance.",
                    'explanation': "Side effects may include: forgetting to eat, sleep, or blink."
                },
                {
                    'title': "Procrastination Elimination",
                    'description': "When there's no more time to procrastinate, developers suddenly discover they can code without watching YouTube tutorials every 5 minutes."
                }
            ],
            
            # Items developers need when working on deadline
            'survival_kit': [
                {"item": "Coffee", "icon": "coffee", "description": "Intravenous preferred"},
                {"item": "Pizza", "icon": "pizza-slice", "description": "Cold is fine"},
                {"item": "Headphones", "icon": "headphones", "description": "Noise-canceling headphones"},
                {"item": "Excuses", "icon": "exclamation", "description": "Excuse generator"},
                {"item": "Sleep", "icon": "bed", "description": "Ability to code while sleeping"}
            ],
            
            # Humorous quotes about deadlines
            'quotes': [
                {"text": "I love deadlines. I like the whooshing sound they make as they fly by.", "author": "Douglas Adams"},
                {"text": "The ultimate inspiration is the deadline.", "author": "Every Developer Ever"},
                {"text": "This would have been done sooner, but my cat sat on my keyboard.", "author": "Anonymous Developer"},
                {"text": "This webpage was created with only 20 minutes left on the deadline, proving everything it claims.", "author": "The Creator"}
            ]
        }
        
        # Return the data as a JSON response
        return Response(data, status=status.HTTP_200_OK)