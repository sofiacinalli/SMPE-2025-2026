Comments/ resume of MOOC 
---

A computational document is a type of file that combines: code, data, results and where the main goal is to enhance transparency and traceability in research.
It allows anyone to access to your data and reports, to reproduce yours experiments, criticize your project and also to continue your work.

Having traceability in yours studies is essential.
It helps to collaborate with transparent analysisis and not forguet what you have done.
It is also usefull to chech your information if somethings goes wrong. 

There are several examples where trazability was missing and their studies failed. Examples of that are:
- Economics - Reinhart & Rogoff (2010) their study claimed that when public debt exceeded 90 % of GDP, economic growth became negative. Later, other researchers tried to replicate it and found several problems: a spreadsheet formula error that excluded five countries, unequal weighting of data, and selective data omissions. Once corrected, the supposed “90 % threshold” disappeared. This case shows the importance of sharing data and code for verification.
- Neuroscience - Dead Fish study. Brain imaging allows us to observe somebody's brain activity while performing a task. It helps us understand how the brain works and its structured. Contrafact: they put a death fish and noticed signs of brain activity. In that moment they realiced that data obtained during an MRI has a lot of noise.If the data and methods had been accessible, the error could have been detected earlier.
- Structural Biology – Geoffrey Chang Case: published several articles in famous magazines about the structure of proteins present in cell membranes. Later, he found different results in others studios and after analysis, he realized that he inherited the code from another lab and it had been used by other teams. Even if the data had been carefully acquired, the analysis had not.

*So transparency is escential to avoid errors in all the studies.*
------
Types of computational documents: 
-
- Jupiter Notebook: useful for combining code, data, and graphs. Can be used in the cloud to share documents. Python is the most common language used.
- RStudio: useful with R and particularly strong for statistical analyses. However, collaborators must install it locally. It uses R, which is powerful but more technical than Python.
- Emacs / org-mode text + code. text + code environment. More technical and harder to learn, but very powerful for creating technical notes and combining text, code, and graphics.

There are some tools used to export HTML/PDF:
- 
- Pandoc: converts documents to pdf/html in Jupyter or RStuudio
- Knitr: creates dynamic documents in R; only works with R.
- LaTex: generates scientific PDFs. For Jupyter or RStudio

This tools are usefull to export documents but they are not when we want to share documentation broadly and include feedback from others.

Then there are some tools to work in colaborative project:
- 
- Git: Vversion control and collaboration. When making a repository public, the entire history is also published, so it must be cleaned before sharing and save a version of what you have submit.
- RPubs: fast and easy for publishing R Markdown documents, but storage is temporary.
- Dropbox: Simple for sharing files. No version control, no guarantee of long-term preservation
- Open Archives (HAL, figshare, Zenodo): long-term repositories for sharing scientific results. They are the best option for durable and citable publications.
  
To choose the best solution, it depends on the coauthors, technical constraints, confidentiality, and copyright considerations.  
And there will be some difficulties but there are solutions, keep trying.

## mooc excercise:
For this Challenger exercise, I chose to work with RStudio. Setting everything up was a bit challenging at first, mainly because I made some mistakes with the GitHub/GitLab connections. Once the environment was configured, I ran into another issue: the package ggplot2 was not installed. When running Error in library(ggplot) because it wasn't built: 
I solved it by installing the package directly in RStudio using: install.packages("ggplot2")

Later, when I tried to export the document to PDF, I realized that I needed additional tools (TinyTeX/LaTeX) to generate the output, which required some extra installation steps.

RStudio seems to have more potential in terms of data analysis and report generation, but coding in R feels a bit more challenging compared to other languages. However, once the environment is correctly set up, the workflow becomes smoother—and the effort pays off, because these tools are essential for producing reproducible and professional documents.
