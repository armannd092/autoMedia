
#!/bin/sh
COUNTER=0
(cd $1 && 
	for FILE in *.mp4; 
	do 
		
		echo $FILE;
		echo $COUNTER;
		ffmpeg -i $FILE -vcodec libx265 -crf 30 $COUNTER.mp4
		((COUNTER++))
	done)
	