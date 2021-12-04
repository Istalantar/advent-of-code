from functions import my_input
import itertools


class Passport:
    REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    def __init__(self):
        self.id = next(passport_nr)
        self.byr = ''
        self.iyr = ''
        self.eyr = ''
        self.hgt = ''
        self.hcl = ''
        self.ecl = ''
        self.pid = ''
        self.cid = ''

    def isValid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid and self.cid

    def isFakeValid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid

    def isNewValid(self):
        return self.isFakeValid() and self.is_byr_eval() and self.is_iyr_eval() and self.is_eyr_eval() \
               and self.is_hgt_eval() and self.is_hcl_eval() and self.is_ecl_eval() and self.is_pid_eval()

    def is_byr_eval(self):
        if not self.byr.isnumeric():
            return False
        elif int(self.byr) < 1920:
            return False
        elif int(self.byr) > 2002:
            return False
        else:
            return True

    def is_iyr_eval(self):
        if not self.iyr.isnumeric():
            return False
        elif int(self.iyr) < 2010:
            return False
        elif int(self.iyr) > 2020:
            return False
        else:
            return True

    def is_eyr_eval(self):
        if not self.eyr.isnumeric():
            return False
        elif int(self.eyr) < 2020:
            return False
        elif int(self.eyr) > 2030:
            return False
        else:
            return True

    def is_hgt_eval(self):
        i_cm = self.hgt.find('cm')
        i_in = self.hgt.find('in')

        if i_cm != -1:
            value = int(self.hgt[:i_cm])
            if value < 150:
                return False
            elif value > 193:
                return False
            else:
                return True
        elif i_in != -1:
            value = int(self.hgt[:i_in])
            if value < 59:
                return False
            elif value > 76:
                return False
            else:
                return True
        else:
            return False

    def is_hcl_eval(self):
        if not self.hcl.startswith('#'):
            return False
        elif len(self.hcl) != 7:
            return False
        elif not str.isalnum(self.hcl[1:]):
            return False
        else:
            return True

    def is_ecl_eval(self):
        COLORS = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        if self.ecl in COLORS:
            return True
        else:
            return False

    def is_pid_eval(self):
        if len(self.pid) != 9:
            return False
        elif not str.isnumeric(self.pid):
            return False
        else:
            return True


def getPassports():
    pass_info = []

    for i in range(len(content)):
        line = content[i]

        if len(line.split()) != 0:  # accumulating info of passport
            pass_info = pass_info + line.split()

        if (line == '') or (i == (len(content) - 1)):  # end of passport or end of file
            this_passport = Passport()

            for info in pass_info:
                field = info.split(':')

                if field[0] == 'byr':
                    this_passport.byr = field[1]
                elif field[0] == 'iyr':
                    this_passport.iyr = field[1]
                elif field[0] == 'eyr':
                    this_passport.eyr = field[1]
                elif field[0] == 'hgt':
                    this_passport.hgt = field[1]
                elif field[0] == 'hcl':
                    this_passport.hcl = field[1]
                elif field[0] == 'ecl':
                    this_passport.ecl = field[1]
                elif field[0] == 'pid':
                    this_passport.pid = field[1]
                elif field[0] == 'cid':
                    this_passport.cid = field[1]

            passports.append(this_passport)
            pass_info = []


def check_valid_passports():
    val = 0
    fake_val = 0
    new_valid = 0
    for passport in passports:
        if passport.isValid():
            val += 1
        if passport.isFakeValid():
            fake_val += 1
        if passport.isNewValid():
            new_valid += 1
    return val, fake_val, new_valid


content = my_input('input.txt')
passport_nr = itertools.count(1)
passports = []
getPassports()
valid_passports, fake_valid_passports, new_valid_passports = check_valid_passports()
print(f'All passports: {len(passports)}')
print(f'Real valid: {valid_passports}')
print(f'Fake valid: {fake_valid_passports}')
print(f'New valid: {new_valid_passports}')
