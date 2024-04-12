import pandas as pd

# Define your data
data ={
    "author": ["Kyle Mercado", "Peter Chuku", "Brianna Lopez", "Jay Estiva", "Ian Cheung"],
    "project_summary": [
        "Create a similar videogame across 3 javascript frameworks to test the viability of creating videogames on webpages for extended usability and accessibility",
        "Impact of different web development frameworks and languages on user engagement and learning outcomes on educational websites through the development of three versions of an educational web application. Triple mod: html/css/js, react, vue",
        "Impact of cryptocurrencies on traditional financial systems and their potential to revolutionize various industries. Triple Mod: slidy, Marp, Python",
        "Explore accessibility guidelines set by WCAG 2.0 and 2.1 and see how well these guidelines are used by today's popular websites and social media. Triple Mod: html/css/js, react, php",
        "Focusing on the Internet of Things and what operating systems and browsers are used. The goal is to display some images and graphics. Trip Mod: google pie chart, bar chart html/CSS, Pie chart excell"
    ],
    "URL": ["https://167.99.253.247/csc543/mercadok9/blank/Assignment5.html#(1)", "https://167.99.253.247/csc543/famuaguno1/Project1%20Final%20Submission.html#(1)", "https://167.99.253.247/csc543/lopezb11/project1/", "https://167.99.253.247/csc543/estivaj1/assignment5/Project1.html#(1)", "http://167.99.253.247/csc543/cheungi1/Project%201/"],
    "CMMI_level": [4, 4, 4, 4, 4],
    "TRL_level": [7, 6, 7, 7, 8],
    "comments": [
        "Very dope and fun project!",
        "I was able to acess implementation 1, nice project very interactive. Was not able to access 2 and 3",
        "All three links work excellent project!",
        "I was not able to access link for imlementation 3. Overall great work!",
        "all three links work excellent project! I like how interacive some of the graphs are!"
    ],
    "questions": [
        "Considering the results of this project, would you recommend a particular framework for developing web-based games, or does it depend on the specific requirements of each project?",
        "How did the choice of web development frameworks (HTML/CSS/JavaScript, React.js, Vue.js) impact the development process and overall user experience of the educational web application?",
        "In your opinion, what are the most promising use cases for cryptocurrencies beyond finance, and how do you envision them revolutionizing various industries in the future?",
        "How do you envision the future of web accessibility, considering the evolving landscape of web development technologies and frameworks?",
        "How did you approach ensuring accessibility and readability in the visualizations, particularly across different devices and screen sizes?"
    ],
     "recommendations": [
        "Consider adding an endpoint to the game that will let users know game is complete. Project is very good with more development it can easily be an 8",
        "Project is very good, if you are able to find a way to make your implementations live this project can be a 6?",
        "I think CMMI and TRL is appropiate for this project!?",
        "I think CMMI and TRL is appropiate for this project! If you can find a solution to make 3rd implementation live it can bump up to an 8",
        "I think CMMI and TRL is appropiate for this project!"
    ],
    

}

df = pd.DataFrame(data)

# Export to CSV
df.to_csv("projects_feedback.csv", index=False)