This program keeps second folder synchronized with main folder.

If you create a new file in main folder. It will copy file to second folder and also synchronizes content of all files (atleast .txt) 

If there is redundant file in second folder, it will be deleted. 



Major flaw of program is that it doesn't work with another folders or rather it can copy folder and its content, however, if we add a file to a new made folder, it wont synchronize. The same is in case of deleting file from a new folder, it won't delete from second folder.

Another major flaw is that if we update content of file, it won't synchronize until there is a new file. I could either synchronize folders every 5 minutes even when there is nothing to synchronize or synchronize every 5 minutes if there is new file to synchronize to replica folder. 


PS: Also logging is little bit messy