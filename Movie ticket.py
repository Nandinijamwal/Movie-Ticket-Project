#include<stdio.h>

void place()
{
int city,theater;
system("color 1e");
printf("\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n\n");
printf("HELLO! WELCOME TO CINEHUB.\n\n");
printf("Choose your city:\n");
printf("\n#1. Jammu\n#2. Chandigarh\n#3. Delhi\n");
printf("\nCity:\t");
scanf("%d",&city);
if(city>0&&city<5)
{

    if(city==1||city==2||city==3)
        {
            theater=center();
                if(theater==1)
                    printf(" WAVE CINEMAS , ");
                if(theater==2)
                    printf(" PVR:KC , ");
                if(theater==3)
                    printf(" MOVIETIME , ");

            if(city==1)
                printf("JAMMU");
            if(city==2)
                printf("CHANDIGARH");
            if(city==3)
                printf("DELHI");

                printf("\n\n\n\n\n");
printf("\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n\n");
        }
    else
        {
            printf("X WRONG OPTION X");
        }
}
return(0);

}


//USER DEFINED FUNCTION TO SELECT THE THEATER.
int center()
{
int theater;
system ("color 2b");
printf("\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n\n");
printf("Choose the theater\t\n");
printf("\n#1. Wave Cinema\n#2. PVR:KC\n#3. Movietime\n#4. Back\n");
printf("\nTheater:\t");
scanf("%d",&theater);


if(theater==4)
    {
        place();
    }
else
    {
        movie();
    }
if (theater==1)
return 1;
if (theater==2)
return 2;
}

// USER DEFINED FUNCTION TO SELECT THE MOVIE.
movie()
{
int film;
system("color 3f");
printf("\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n\n");
printf("These are the latest movies in the theater. Choose the movie you would like to watch:\n");
printf("\n#1. Avatar: The Way of Water\n#2. M3GAN\n#3. The Women King\n#4. Back\n");
printf("\nFilm:\t");
scanf("%d",&film);

if(film==4)
    {
        center();
    }
else
    {
        screen();
    }
}

// USER DEFINED FUNCTION TO SELECT THE SCREEN.
screen()
{
int scr;
system("color 5b");
printf("\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n\n");
printf("Choose the Screen:\n");
printf("\n#1. Screen 1\n#2. Screen 2\n#3. Screen 3\n#4. Back\n");
printf("\nScreen:\t");
scanf("%d",&scr);

if(scr==4)
    {
        movie();
    }
else
//USE  TO SELECT TIME OF BOOKING.
    {
        int selected_time,step,i,tickets;
        char* row,sno[280];
        char* time[]={"0:\t10.00-1.00","1:\t1.10-4.10","2:\t4.20-7.20","3:\t7.30-10.30","4:\t10:45-12:45"};
        system("color 5e");
        printf("\n*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n\n");

// NUMBER OF TICKETS USER WISH TO BOOK.
        system("color 0d");
        printf("\n\nHow many Tickets you would like to book? :\t");
        scanf("%d",&tickets);
        printf("TIMINGS:\n\n");
        for(int i=0;i<5;i++)
            {
                printf("\t%s\n",time[i]);
            }
        printf("\n\nKindly select Time:\t");
        scanf("%d",&selected_time);

// DISPLAYING THE PRICES OF TICKETS ACCORDING TO THE DIVISION OF SEATS.
        system("color 6f");
        printf("\n\nFront block- Rs.180/-\nMiddle block- Rs.220/-\nBehind- Rs.380/-\n\n");
        printf("Select seat block:\n1. Front\n2. Middle\n3. Behind\n");
        printf("Select:\t");
        scanf("%d",&step);

//INPUT THE DESIRED SEATS.

if(step==1)
    {
        printf("Choose Row from (A TO I):\t");
        scanf("%s",&row);
        if(65<=row||row<=74)
            {
                printf("SELECTED!\n");
            }
        else
            {
                printf("ERROR");
                exit(1);
            }
        for(i=0;i<tickets;i++)
            {
                printf("Choose Seat number: (1-10):\t");
                scanf("%s",&sno[i]);
            }
    }
else if(step==2)
    {
        printf("Choose Row from (J TO R):\t");
        scanf("%s",&row);
        if(75<=row||row<=84)
        {
            printf("SELECTED!\n");
        }
        else
        {
            printf("ERROR");
            exit(1);
        }
        for(i=0;i<tickets;i++)
        {
            printf("Choose Seat number: (1-10):\t");
            scanf("%s",&sno[i]);
        }
    }
else
    {
        printf("Choose Row from (S TO Z):\t");
        scanf("%s",&row);
        if(85<=row||row<=93)
            {
                printf("SELECTED!\n");
            }
        else
            {
                printf("ERROR");
                exit(1);
            }
        for(i=0;i<tickets;i++)
            {
                printf("Choose Seat number: (1-10):\t");
                scanf("%s",&sno[i]);
            }
    }
system("color 4e");
printf("\n\n\n");
printf("\n\n\n YOUR TOTAl PAYABLE AMOUT IS:\n");
if(step==1)
    {step=180;
    step=step*tickets;}
if(step==2)
    {step=220;
    step=step*tickets;}
if(step==3)
    {step=380;
    step=step*tickets;}
printf(" %d /- RUPEES",step);
printf("\n\n Ticket(s) has been booked Successfully! \n\n\n Enjoy your movie at: %s\n SCREEN :%d \n",time[selected_time],scr);
    }

}

//USE DRFINED FUNCTION TO SELECT TIME OF BOOKING.




//THE MAIN FUNCTION
main()
{
int option,pnr;
system("color 5f");
printf("\t\t*** TICKET BOOKING SYSTEM ***\n\n");
printf("KINDLY CHOOSE:-\n\n1. PNR status\n2. Ticket booking\n\n");
printf("Your Choice:\t");
scanf("%d",&option);
if(option==1)
{
printf("\nEnter your PNR number:\t");
scanf("%d",&pnr);
printf("\nTHANKYOU! YOUR PNR STATUS WILL BE SENT TO THE REGISTERED MOBILE NUMBER.\n");
}
else
{
place();
}
}
