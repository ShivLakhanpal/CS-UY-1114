John_days = int(input('Please enter the number of days John has worked: '))
John_hours = int(input('Please enter the number of hours John has worked: '))
John_minutes = int(input('Please enter the number of minutes John has worked: '))
Bill_days = int(input('Please enter the number of days Bill has worked: '))
Bill_hours = int(input('Please enter the number of hours Bill has worked: '))
Bill_minutes = int(input('Please enter the number of minutes Bill has worked: '))

minutes_total = John_minutes + Bill_minutes
minutes_less_than_60 = minutes_total%60
hour_extra = minutes_total//60
hours_total = John_hours + Bill_hours + hour_extra
hours_less_than_24 = (John_hours + Bill_hours)%24+hour_extra
extra_day = hours_total//24
total_days = John_days + Bill_days + extra_day

print('The total time both of them worked together is: ', str(total_days) \
      + 'days, ',str(hours_less_than_24) + 'hours and ',\
      minutes_less_than_60,'minutes.')
