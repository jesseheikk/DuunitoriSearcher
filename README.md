# DuunitoriSearcher

A simple web scraping example using Python/Selenium in a Vagrant/VirtualBox environment.

This program executes a search in "duunitori.fi" and saves the search results in a CSV file (first page only).

<h2>How to run</h2>

Once inside the repository, initiate the Vagrant machine
> vagrant up

ssh inside the machine
> vagrant ssh

Run the app
> python3 /srv/mount_folder/job_searcher.py

The results will be saved in a file named "search_results.csv"
