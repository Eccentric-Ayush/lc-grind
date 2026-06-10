class Solution:
    def leapyear(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    def dayOfYear(self, date: str) -> int:
        if not self.leapyear(int(date[:4])):
            if date[5]=='0' and date[6]=='1':
                return int(date[8:])
            if date[5]=='0' and date[6]=='2':
                return int(date[8:])+31
            if date[5]=='0' and date[6]=='3':
                return int(date[8:])+59
            if date[5]=='0' and date[6]=='4':
                return int(date[8:])+90
            if date[5]=='0' and date[6]=='5':
                return int(date[8:])+120
            if date[5]=='0' and date[6]=='6':
                return int(date[8:])+151
            if date[5]=='0' and date[6]=='7':
                return int(date[8:])+181
            if date[5]=='0' and date[6]=='8':
                return int(date[8:])+212
            if date[5]=='0' and date[6]=='9':
                return int(date[8:])+243
            if date[5]=='1' and date[6]=='0':
                return int(date[8:])+273
            if date[5]=='1' and date[6]=='1':
                return int(date[8:])+304
            if date[5]=='1' and date[6]=='2':
                return int(date[8:])+334
        else:
            if date[5]=='0' and date[6]=='1':
                return int(date[8:])
            if date[5]=='0' and date[6]=='2':
                return int(date[8:])+31
            if date[5]=='0' and date[6]=='3':
                return int(date[8:])+60
            if date[5]=='0' and date[6]=='4':
                return int(date[8:])+91
            if date[5]=='0' and date[6]=='5':
                return int(date[8:])+121
            if date[5]=='0' and date[6]=='6':
                return int(date[8:])+152
            if date[5]=='0' and date[6]=='7':
                return int(date[8:])+182
            if date[5]=='0' and date[6]=='8':
                return int(date[8:])+213
            if date[5]=='0' and date[6]=='9':
                return int(date[8:])+244
            if date[5]=='1' and date[6]=='0':
                return int(date[8:])+274
            if date[5]=='1' and date[6]=='1':
                return int(date[8:])+305
            if date[5]=='1' and date[6]=='2':
                return int(date[8:])+335