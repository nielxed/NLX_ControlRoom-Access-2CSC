"""
As taken from ChatGPT:
In this example, the CounterManager class has a dictionary attribute named counter_dict with
three keys ('key1', 'key2', 'key3'), all initialized to 0. The increment_key method takes a key
and increments its associated value by 1. The get_values method returns the current values of 
all keys in the dictionary.

You can create an instance of CounterManager, use the increment_key method to increment values
associated with different keys, and then use the get_values method to retrieve the current values.
"""
# class CounterManager:
#     def __init__(self, initial_values=None):
#         if initial_values is None:
#             initial_values = {'key1': 0, 'key2': 0, 'key3': 0}
#         self.counter_dict = initial_values

#     def increment_key(self, key):
#         # Increment the value associated with the specified key by 1
#         if key in self.counter_dict:
#             self.counter_dict[key] += 1
#         else:
#             print(f"Key '{key}' not found in the dictionary.")

#     def get_value(self, key):
#         # Return the current value associated with the specified key
#         return self.counter_dict.get(key, None)

# # Example usage:
# counter_manager = CounterManager()

# # Increment values dynamically
# counter_manager.increment_key('key1')
# counter_manager.increment_key('key2')
# counter_manager.increment_key('key3')
# counter_manager.increment_key('key1')

# # Get and print the value for a specific key
# value_for_key2 = counter_manager.get_value('key2')
# print("Current value for 'key2':", value_for_key2)

class CamCounterManager:
    def __init__(self, initial_values=None):
        if initial_values is None:
            initial_values = {'rbt_CSC_11101':0, 'rbt_CSC_11103':0, 'rbt_CSC_11104':0, 'rbt_CSC_11105':0, 'rbt_CSC_11106':0, 'rbt_CSC_11108':0,\
                            'rbt_CSC_11109':0, 'rbt_CSC_111011':0, 'rbt_CSC_111012':0, 'rbt_CSC_111013':0, 'rbt_CSC_111015':0, 'rbt_CSC_111017':0,\
                            'rbt_CSC_111019':0, 'rbt_CSC_111025':0, 'rbt_CSC_111028':0, 'rbt_CSC_111029':0, 'rbt_CSC_111031':0, 'rbt_CSC_111033':0,\
                            'rbt_CSC_111034':0, 'rbt_CSC_111035':0, 'rbt_CSC_111036':0, 'rbt_CSC_111037':0, 'rbt_CSC_111040':0, 'rbt_CSC_111042':0,\
                            'rbt_CSC_111043':0, 'rbt_CSC_111044':0, 'rbt_CSC_111045':0, 'rbt_CSC_111046':0, 'rbt_CSC_111048':0, 'rbt_CSC_11202':0,\
                            'rbt_CSC_11203':0, 'rbt_CSC_11204':0, 'rbt_CSC_11206':0, 'rbt_CSC_11208':0, 'rbt_CSC_11209':0, 'rbt_CSC_112010':0,\
                            'rbt_CSC_112011':0, 'rbt_CSC_112013':0, 'rbt_CSC_112014':0, 'rbt_CSC_112016':0, 'rbt_CSC_112017':0, 'rbt_CSC_112020':0,\
                            'rbt_CSC_112021':0, 'rbt_CSC_112022':0, 'rbt_CSC_112023':0, 'rbt_CSC_112024':0, 'rbt_CSC_112025':0, 'rbt_CSC_112026':0,\
                            'rbt_CSC_112027':0, 'rbt_CSC_112028':0, 'rbt_CSC_112029':0, 'rbt_CSC_112030':0, 'rbt_CSC_112031':0, 'rbt_CSC_112032':0,\
                            'rbt_CSC_112033':0, 'rbt_CSC_112034':0, 'rbt_CSC_112035':0, 'rbt_CSC_112036':0, 'rbt_CSC_112038':0, 'rbt_CSC_112040':0,\
                            'rbt_CSC_112042':0, 'rbt_CSC_113011':0, 'rbt_CSC_113013':0, 'rbt_CSC_113015':0, 'rbt_CSC_113017':0, 'rbt_CSC_113019':0,\
                            'rbt_CSC_113033':0, 'rbt_CSC_113034':0, 'rbt_CSC_113036':0, 'rbt_CSC_113037':0, 'rbt_CSC_113038':0, 'rbt_CSC_113039':0,\
                            'rbt_CSC_113040':0, 'rbt_CSC_113041':0, 'rbt_CSC_113042':0, 'rbt_CSC_113043':0, 'rbt_CSC_113044':0, 'rbt_CSC_111045':0,\
                            'rbt_CSC_14101':0, 'rbt_CSC_14102':0, 'rbt_CSC_14103':0, 'rbt_CSC_14104':0, 'rbt_CSC_14105':0, 'rbt_CSC_14106':0,\
                            'rbt_CSC_14107':0, 'rbt_CSC_14109':0, 'rbt_CSC_141010':0, 'rbt_CSC_141011':0, 'rbt_CSC_141013':0, 'rbt_CSC_141014':0,
                            'rbt_CSC_141015':0, 'rbt_CSC_141017':0, 'rbt_CSC_141018':0, 'rbt_CSC_141019':0, 'rbt_CSC_141020':0, 'rbt_CSC_141021':0,\
                            'rbt_CSC_141022':0, 'rbt_CSC_141023':0, 'rbt_CSC_141024':0, 'rbt_CSC_141025':0, 'rbt_CSC_141027':0, 'rbt_CSC_141029':0,\
                            'rbt_CSC_141031':0, 'rbt_CSC_141033':0, 'rbt_CSC_141035':0, 'rbt_CSC_141037':0, 'rbt_CSC_141039':0, 'rbt_CSC_141041':0,\
                            'rbt_CSC_141043':0, 'rbt_CSC_141044':0, 'rbt_CSC_141045':0, 'rbt_CSC_141046':0, 'rbt_CSC_14201':0, 'rbt_CSC_14203':0,\
                            'rbt_CSC_14205':0, 'rbt_CSC_14207':0, 'rbt_CSC_142010':0, 'rbt_CSC_142011':0, 'rbt_CSC_142013':0, 'rbt_CSC_142015':0,\
                            'rbt_CSC_142017':0, 'rbt_CSC_142018':0, 'rbt_CSC_142019':0, 'rbt_CSC_142021':0, 'rbt_CSC_142022':0, 'rbt_CSC_142025':0,\
                            'rbt_CSC_142027':0, 'rbt_CSC_142028':0, 'rbt_CSC_142032':0, 'rbt_CSC_142033':0, 'rbt_CSC_142035':0, 'rbt_CSC_142036':0,\
                            'rbt_CSC_142037':0, 'rbt_CSC_142038':0, 'rbt_CSC_142040':0,\
                            'rbt_CSC_13101':0, 'rbt_CSC_13102':0, 'rbt_CSC_13103':0, 'rbt_CSC_13104':0, 'rbt_CSC_13105':0, 'rbt_CSC_13106':0,\
                            'rbt_CSC_13107':0, 'rbt_CSC_13108':0, 'rbt_CSC_13109':0, 'rbt_CSC_131011':0, 'rbt_CSC_131013':0, 'rbt_CSC_131015':0,\
                            'rbt_CSC_131017':0, 'rbt_CSC_131019':0, 'rbt_CSC_131021':0, 'rbt_CSC_131039':0, 'rbt_CSC_131041':0, 'rbt_CSC_131043':0,\
                            'rbt_CSC_20102':0, 'rbt_CSC_20103':0, 'rbt_CSC_20104':0, 'rbt_CSC_20105':0, 'rbt_CSC_20106':0, 'rbt_CSC_20107':0,\
                            'rbt_CSC_20108':0, 'rbt_CSC_20109':0, 'rbt_CSC_201010':0, 'rbt_CSC_201011':0, 'rbt_CSC_201012':0, 'rbt_CSC_201013':0,\
                            'rbt_CSC_201014':0,\
                            'rbt_CSC_4104':0, 'rbt_CSC_4107':0, 'rbt_CSC_4103':0, 'rbt_CSC_4102':0, 'rbt_CSC_4101':0, 'rbt_CSC_4108':0,\
                            'rbt_CSC_4106':0,\
                            'rbt_CSC_3101':0, 'rbt_CSC_3102':0, 'rbt_CSC_3103':0, 'rbt_CSC_3104':0, 'rbt_CSC_3105':0, 'rbt_CSC_3106':0,\
                            'rbt_CSC_3107':0, 'rbt_CSC_3108':0, 'rbt_CSC_31010':0, 'rbt_CSC_31011':0, 'rbt_CSC_31012':0,\
                            'rbt_CSC_40101':0, 'rbt_CSC_40105':0, 'rbt_CSC_40106':0, 'rbt_CSC_40108':0, 'rbt_CSC_40109':0, 'rbt_CSC_401017':0,\
                            'rbt_CSC_401019':0, 'rbt_CSC_401023':0, 'rbt_CSC_41017':0, 'rbt_CSC_41019':0, 'rbt_CSC_41021':0, 'rbt_CSC_41022':0,\
                            'rbt_CSC_41023':0, 'rbt_CSC_41024':0,\
                            'rbt_CSC_72017':0, 'rbt_CSC_72018':0, 'rbt_CSC_72019':0, 'rbt_CSC_72020':0, 'rbt_CSC_72021':0, 'rbt_CSC_72022':0,\
                            'rbt_CSC_72023':0, 'rbt_CSC_73017':0, 'rbt_CSC_73018':0, 'rbt_CSC_73019':0, 'rbt_CSC_73020':0, 'rbt_CSC_73021':0,\
                            'rbt_CSC_73022':0, 'rbt_CSC_73023':0, 'rbt_CSC_73024':0, 'rbt_CSC_74017':0, 'rbt_CSC_74018':0, 'rbt_CSC_74020':0,\
                            'rbt_CSC_74021':0, 'rbt_CSC_74022':0, 'rbt_CSC_74023':0,\
                            'rbt_CSC_100017':0, 'rbt_CSC_100019':0, 'rbt_CSC_100021':0, 'rbt_CSC_100023':0, 'rbt_CSC_101017':0, 'rbt_CSC_101018':0,\
                            'rbt_CSC_101020':0, 'rbt_CSC_101022':0, 'rbt_CSC_101024':0
                            }
        self.counter_dict = initial_values

    def increment_key(self, key):
        # Increment the value associated with the specified key by 1
        if key in self.counter_dict:
            self.counter_dict[key] += 1
        else:
            print(f"Key '{key}' not found in the dictionary.")

    def get_value(self, key):
        # Return the current value associated with the specified key
        return self.counter_dict.get(key, None)

# Example usage:
counter_manager = CamCounterManager()
