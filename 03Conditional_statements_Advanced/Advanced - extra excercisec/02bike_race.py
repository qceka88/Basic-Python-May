cyclics_jr = int(input())
cyclics_snr = int(input())
race_track = input()

total_cyclist = cyclics_jr + cyclics_snr
tax_jr = 0
tax_snr = 0

if race_track == "trail":
    tax_jr = cyclics_jr * 5.50
    tax_snr = cyclics_snr * 7
elif race_track == "cross-country":
    tax_jr = cyclics_jr * 8
    tax_snr = cyclics_snr * 9.5
    if 50 <= total_cyclist:
        tax_jr=tax_jr*0.75
        tax_snr=tax_snr*0.75
elif race_track == "downhill":
    tax_jr = cyclics_jr * 12.25
    tax_snr = cyclics_snr * 13.75
elif race_track == "road":
    tax_jr = cyclics_jr * 20
    tax_snr = cyclics_snr * 21.50

tax_total = tax_jr + tax_snr
expenses = tax_total * 0.95


print(f"{expenses:.2f}")
