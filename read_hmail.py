from pathlib import Path
import sys
import re

exch = 4.85

def main():
    
    if len(sys.argv) < 2:
        print('File not found. ')
        exit()
    
    file_to_read = Path(sys.argv[1])
    read_file(file_to_read)

def read_file(file : Path):
    
    with open(file, 'r') as calculation:

        founded_prices = []
        
        calc = calculation.readlines()

        for raws in calc:

            price = re.findall(r'\d{1,3}[x]\s\d{1,3}[,]\d{2}', raws)
            if price:
                founded_prices.append(price)

        calc_end_price(founded_prices)

def calc_end_price(price_in_pln : list):

        preparation = ''.join(price_in_pln[0])
        price_piece = ''.join(price_in_pln[1])

        for num in preparation: 
            if num.isdigit():
                continue
            elif num == ',' or num == ' ':
                continue
            else:
                preparation = preparation.replace(num, '')
                preparation = preparation.replace(',', '.')

        for num in price_piece: 
            if num.isdigit():
                continue
            elif num == ',' or num == ' ':
                continue
            else:
                price_piece = price_piece.replace(num, '')
                price_piece = price_piece.replace(',', '.')

        preparation = preparation.split(' ')
        price_piece = price_piece.split(' ')

        nums_in_pln = []

        for pln in preparation:
            pln = float(pln)
            nums_in_pln.append(pln)
        
        for pcs in price_piece:
            pcs = float(pcs)
            nums_in_pln.append(pcs)

        final_price(nums_in_pln)

def final_price(cprice : list) -> float:
    
    prep_cost = round((cprice[0] * cprice[1]) / exch / cprice[2], 2)
    pc_cost = round(cprice[3] / exch, 2)
    final_price = prep_cost + pc_cost + 0.10
    
    print(f'The final price for the customer is {final_price} EUR.')

    mail_for_customer(final_price)

def mail_for_customer(price_for_c : float):

    text = 'Dear Customer, \n\n'\
        f'The price for printing service is {price_for_c} euro/pc. \n\n'\
        'The production time is 10-15 business days. If you agree with price and terms, '\
        'please, place the order in the E-shop and we`ll prepare the mock-up. \n\n'\
        'Best regards, \n\n'\
        'Serhii Levytskyi\n'\
        'Malfini, a.s. '

    with open('Mail.doc', 'w', encoding='utf-8') as mail:

        mail.write(text)


if __name__ == '__main__':
    main()
    print('Good job!')