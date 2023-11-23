# BH3_pictures_archive
Archive of pictures posted on miyoushe.com
# Updated 11/23/2023
Mega link:

https://mega.nz/folder/JWMnCRaZ#xm4xhiIBtLC1q-C6pnsqFQ

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

2) download with python file provided

Sometimes the title contain bad characters, for example the sigmata. Since it only happen in earlier posts and does not happen too often, I just manually fix them.

3) change the dates if you wish

year is omitted for 2023, so for completeness I append those with the powershell command.

Finally, if you feel this helped you, please star this repo! Thanks!
