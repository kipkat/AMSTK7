# AMSTK7
Python Encryption Algorithm - Fast, secure and impossible to reverse
# Usage
```py
>>> from amstk import *
>>> amstk7('password')
'MMI1GMI85381E395M61GM805EEG5E5M3MM65E65E85E5W87561638I18Q715IE10'
>>> amstk7('password',16) # last 16 chars
'61638I18Q715IE10'
>>> amstk7('test',16)
'2560111MAA2OMM2Q'
>>> amstk7('abc')
'229941398Q1818965K3Q883S2K091Q492239M1Q990W334Q24K03K3Q9294QK314'
>>> amstk7('abb') # 'ab' in common but no connection between them
'2931M323MK27EQ23Q95131123Q39K7K772Q3E12Q1251QEQ12A2Q892QAA321Q33'
>>> amstk7('000000000000000001')
'M91QAQQA40I2863EA442M04MA78821230A362E96521148106611QQ34M29M6318'
>>> amstk7('000000000000000010') # will give a completely different string with no connection with the first one
'68116M1QA02232720A1Q8241Q3444A1828472M08QQ6AQ21466QM512871EI1231'
>>> seed_amstk7('test',1)==amstk7('test')
False
>>> seed_amstk7('test',0)==amstk7('test') # seed 0 is the same with...
True
>>> seed_amstk7('test',250001) # changes the seed
'12C5212A41AMO450EM43A33171OQ9MO24241Q6Q13E326185E59124E22721E613'
>>> repeat_amstk7('test',2)==amstk7(amstk7('test')) # same thing
True
>>> repeat_amstk7('test',150) # repeats algorithm 150 times
'6991GAA9G84A4AAUA620A39A91A7AY2331A92A71398A1A14A3482128A9919710'
```
