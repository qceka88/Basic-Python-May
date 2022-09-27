sheets_quantiy=int(input())
sheets_per_hour=int(input())
days=int(input())
book_time=sheets_quantiy/sheets_per_hour
requried_hours=book_time//days
print(requried_hours)