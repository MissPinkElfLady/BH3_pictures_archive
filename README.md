# BH3_pictures_archive
Archive of Honkai Impact 3 pictures posted on miyoushe.com

# Mega link for preview/download the pictures:
Updated 11/23/2023

https://mega.nz/folder/JWMnCRaZ#xm4xhiIBtLC1q-C6pnsqFQ

# Continue reading if you want to do it yourself:
json scraped with ParseHub (note that parsehub only supports 200 pages for the free version so you may need to run couple times to get the full result)

downloaded with python script

Usage:

1) scraping the json files containing main page and picture links

open the .phj file with ParseHub and run
listingValue is used to control when to refresh the page, refer to tutorial here 
https://help.parsehub.com/hc/en-us/articles/115005473287-Infinite-Scroll

logValue is used to bypass the 200 page limit. It is defined in the third line of main_template and should have initial value of 0. Specifically, open the json from last run and replace the if statement before the middle extract logValue to $e.text=="insert_last_page_name_here" and make sure logValue is set to 1 after the if statement.

The second if statement filters the wanted word in title and only scrapes those pages in photo_scrape.

You might want to join the json files from different runs for the download to be easier.

If you want to take a look at what a scrape looks like, I have included a json file that contains info for all posts from the official account I scraped. Image links are for wallpapers and can be found in the wallpaper folder in mega. 

2) download with download_images_with_retry.py

Sometimes the title contain bad characters, for example the sigmata. Since it only happen in earlier posts and does not happen too often, I just manually fix them.

Rarely does an image exceed maximum number of tries. You could try and increase MAX_RETRIES if you want. Alternatively the script also prints out failed pictures along with their assigned names so you can manually download them if there are not too many failed attempts.

3) change the dates if you wish

year is omitted for 2023, so for completeness I append those with the powershell command.

# Important: 

Parsehub somehow does not get the job done and a lot of posts that should have image urls do not have them. I am working on making another script to replace its job. Current remedy is to use other scripts to check and redownload:

Run the find_parsehub_omittance.py to generate a json that contains list of urls that are not downloaded

Load the json file into miyoushe_individual_page_scrape.py

Often times the connection will time out. The script will save failed entries and output it to another file, and you can load it back into the script again to rerun. Often times this will solve the issue. I did not set it up recursively such that even if something happens, at least part of the output is still accessible.

Use the download_images_with_retry.py to repeat the process again.

Finally, run the powershell command to append current year to the filenames if you wish.

If you feel this helped you, please star this repo! Thanks!
