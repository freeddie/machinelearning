#include "types.h"
#include "stat.h"
#include "user.h"

char buffer[500];  

void printFile(int fd,int lines);

int main(int argc, char *argv[])
{
	int fd=0;//no file descriptor in default, so read data from input
	int	lines=10; // read 10 lines of data in default

	if(argc <=1)
	{
		printFile(fd,lines);
		exit();
	}

	for(int i=1;i<argc;i++)
	{
		if(atoi(argv[i]) == 0)//????
		{
			if(fd=open(argv[i],0)<0)
			{
				printf(1,"head:cannot openfile %s\n",argv[i]);
				exit();
			}

		}
		else //it's a number with "-" in the front
		{
			lines=atoi(argv[i]*-1);
		}
	}
	head(fd,lines);
	close(fd);
	exit();

}
//print the n lines of a given file
void printFile(int fd,int lines)
{
	char str[500];
	int totalBytes;
	totalBytes = read(fd,buffer,sizeof(buffer));
	if(totalBytes <= 0)
		printf(1,"/s","the file is empty");
		return
	for(i=0;i<totalBytes;i++)
	{
		int j = 0; //index of str[]
		int printedLine = 0;
		if buffer[i] != "\n"
		{
			str[j] = buffer[i];
			j++;
		}
		else
		{
			printf(1,"%s/n",str);
			printedLine++;
			//reset the str
			j=0;
			memset(string, 0, 512);
		}
		if(printedLine==lines)
		{
			exit();
		}

	}
}
