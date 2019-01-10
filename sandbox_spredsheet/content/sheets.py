class Sample:
    SHEET_NAME = 'SampleSheet'

    @classmethod
    def nowTime(self, fieldNumber=1):
        if fieldNumber <= 0:
            print('フィールドは１以上を指定してください')
            return
        return 'A{0}'.format(fieldNumber)

    @classmethod
    def uptime(self, fieldNumber=1):
        if fieldNumber <= 0:
            print('フィールドは１以上を指定してください')
            return
        return 'B{0}'.format(fieldNumber)

    @classmethod
    def users(self, fieldNumber=1):
        if fieldNumber <= 0:
            print('フィールドは１以上を指定してください')
            return
        return 'C{0}'.format(fieldNumber)

    @classmethod
    def loadAverage(self, fieldNumber=1):
        if fieldNumber <= 0:
            print('フィールドは１以上を指定してください')
            return
        return 'D{0}'.format(fieldNumber)

    @classmethod
    def nowDateTime(self, fieldNumber=1):
        if fieldNumber <= 0:
            print('フィールドは１以上を指定してください')
            return
        return 'E{0}'.format(fieldNumber)