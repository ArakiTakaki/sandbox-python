class Sample:
    SHEET_NAME = 'SampleSheet'

    @classmethod
    def cpu(self, fieldNumber=1):
        if fieldNumber <= 0:
            print('フィールドは１以上を指定してください')
            return
        return 'A{0}'.format(fieldNumber)

    @classmethod
    def memory(self, fieldNumber=1):
        if fieldNumber <= 0:
            print('フィールドは１以上を指定してください')
            return
        return 'B{0}'.format(fieldNumber)
