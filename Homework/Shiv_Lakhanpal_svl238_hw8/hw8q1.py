#Shiv Lakhanpal
#svl238
#hw8q1.py

'''This code consists of 4 parts, a, b, c, d. The first part asked me to create
a monthly calender which included the day of the week and the days. The second
part asked me to determine if a certain year is considered a leap year or not.
If it was a leap year it returns true, if it isn't it returns false. The third
problem asked me to create a whole calendar based on the certain year and the
final part interacted with the user and asked it to input a year and enter a
number from 1 to 7 (Mo-Sun) and it would print out the calender.'''




def Calendar(days, start):
      print('Mo','Tu','We','Th','Fr','Sa','Su', sep='\t')
      nextmonth_start = 1
      for i in range(1,start):
            print('\t',end='')
            nextmonth_start = nextmonth_start+1
      for i in range(1,days+1):
            if nextmonth_start == 7:
                  print('%d\t'%i)
                  nextmonth_start = 0
            else:
                  print('%d\t'%i,end='')
            
            nextmonth_start = nextmonth_start+1
      print('')
      return nextmonth_start
      

def Gregorian(year):
      if year % 4 == 0 and year % 100 != 0:
            return True
      elif year % 4 == 0 and year % 400 == 0:
            return True
      else:
            return False

def YearlyCalendar(year, start):
      months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
      for i in range(1,13):
            print('\t%s %d'%(months[i-1],year))
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                start = Calendar(31, start)
            elif i == 4 or i == 6 or i == 9 or i == 11:
                start = Calendar(30, start)
            elif Gregorian(year) == True:
                start = Calendar(29, start)
            else:
                start = Calendar(28, start)

def main():
        year = int(input('What year is it? '))
        start = int(input('What day does the year start on (please enter 1-7 for Mo-Sun)? '))
        YearlyCalendar(year, start)

main()
