# DevaintArt_bot


**** Description ****

This bot is supposed to download pictures from a given DevaintArt gallery. Runs on Windows and Linux (not tested on macOS). Comes 'as is', the code is not refactored and structured properly. Crashes may occur.



**** Installing ****

This code include the "bs4" and "requests" modules, what you might need to install to your machine, especially under Windows.
To do this, you can follow this tutorial: https://www.quora.com/What-is-the-step-by-step-procedure-to-install-Beautiful-Soup-In-Windows or search another one. You can install the "requests" module just like the "bs4".



**** Usage ****

To run the program, simply put the main.py file to a choosen folder, double click it, or run from the terminal. Under normal circumstances, the program will ask for an artist's name; while this is not case sensitive, it is recommended to copy-paste the artist's name from DeviantArt, because the program will make a folder named accoring to this input. After you typed or pasted the right name, press enter. 
If the name incorrect, the download is not possible, however you can exit and start the program again anytime. If you don't give any input, the program will requests again, while you don't give at least one character. If you insist to exit anyway, close the terminal or press "ctrl+c" to terminate the running.

Then the program will check the 'main gallery', and the 'scrap gallery'. After fetched out the links, it will start to download the pictures one by one.

Please note only the so called "Safe For Work" pictures will be downloaded.



**** Files ****

main.py: This is the main file. Place this file where you want to save the pictures.

download_log.txt: at the first run ever, the program will make this file to log what pictures are downloaded previously from a given gallery. If you ask the program to check if there is a new picture or not since the last download in a given gallery, the program will ignore the source links included in this file. Deleting a link(s) from this file will result downloading that picture again.
If you replace the main.py, please move this file with that, or the program will assume that it is the first run, and make the file again at the new place.



**** Messages ****

RESPONSE GET ------------------------ No.  (number)
STATUS CODE --  (http status code)
The code asking data from the server. Due to the DA1s limitation, the server send only 24 picture at once, therefore the code will make another request while there are more pictures in the gallery. The (number) is the number of the package, the (http status code) is obvious. 
If there are no more picture in the gallery, the server will not send data, and you will see an "RESPONSE GOT WITH NO VALUABLE DATA! REQUESTING FINISHED" message.
If the status code is "200", but you don't get any data, it means the gallery is empty.
If the status code is "404", then you most likely mistyped the artist's name. Or simply not connected to the internet.

After that will give you the found link.

NUMBER OF LINKS FOUND ---------------- (number)
Total number of links found.

NUMBER :: (number)    PROGRESS :: (percantage)
Inform you about the progress and how many picture is processed so far.

FETCHED LINK:  (link)
Inform you that the code started to search the source link.

DOWNLOADING ------------------- [(link)]
Inform you if the source link is found, check if the file was downloaded or not previously, starting to download if not.

SAVED AS: (filepath and name)
Inform you if the file is succesfull downloaded, and where can you find it (please note it's a realtive path, start the searching in folder where your main.py file is placed)

Alternative messages instead of "SAVED AS:"
  - "This file has already been downloaded!"
    It means the file has been downloaded previously. Will not download again. If you wish to download again you need to open the "download_log.txt" file, manually delete the source link(s), and run the porgram again with the same user name.

  - "This is not a picture or NSFW content"
    The program does not download NSFW pictures or non-pictures.

  - "Failed to download: Error (http status code) "
    Failed to download due to a connection error. You can try again by running the program later.

"Download logged!"
If the file is succesfully downloaded, it will be logged to the "download_log.txt" to avoid unnecessary downloading in the future.

"OK"
If the program successfull ended, you will get this message.



**** License ****
This code is under MIT license, read LICENSE.txt file for more info.




