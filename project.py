print("Name of the jewellery store is 'Bhairava silver merchant'")
print("Location :- Kamareddy\n")
print("list of metals available")
print("- gold\n" + "- silver\n")
condition = input("enter 'g' for gold and 's' for silver if both enter 'b' : ")


if condition == "g":   
    class list_gold_ornaments():
        
        def __init__(self):
            self.ornaments = []
            
        def list_g_ornaments(self):
            print("\nlist of gold ornaments available")
            for ornament in self.ornaments:
                print("- " + ornament)
            print("\n")  
    my_list = list_gold_ornaments()
    my_list.ornaments = ["Bangles","Chains","Earrings","Rings","Haaram","Necklaces",
                        "Ottiyanam","Pendant","Ruby & Emerald","Vanki"]
    my_list.list_g_ornaments()
             
    class gold_ornament():
    
        def __init__(self,need_item,m_g_rate,kt,w_grms,wstge_per,mak_charges_per_grm):
            self.need_item = need_item
            self.t_amount = 0
            self.t_amount_gst = 0 
            self.p_gold = 0
            self.m_g_rate = m_g_rate
            self.kt = kt
            self.w_grms = w_grms
            self.t_weight = 0
            self.wstge = 0
            self.wstge_per = wstge_per
            self.mak_charges = 0
            self.mak_charges_per_grm = mak_charges_per_grm
            self.gst_per = 3
            self.gst = 0
            self.sub_t_amount = 0
                
        
        def market_gold_rate(self):
            print("\n\t***  Total bill details  ***\n")
            print("\nToday's market gold rate :- " + str(self.m_g_rate))
            
        def carat(self):
            print("Carat :- " + str(self.kt))   
                 
        def gold_price(self):
            self.p_gold = (self.kt/24)*self.m_g_rate
            print("\nGold price :- " + str(self.p_gold))
            
        def carat(self):
            print("Carat :- " + str(self.kt))
            
        def weight(self):
            print("Weight(grms) :- " + str(self.w_grms))
            
        def total_weight(self):
            self.t_weight = self.w_grms+self.wstge
            print("Total weight including wastage(grms) :- " + str(self.t_weight))
            
        def wastage_percentage(self):
            print("Wastage(%) :- " + str(self.wstge_per))
            
        def wastage(self):
            self.wstge = self.w_grms*self.wstge_per/100
            print("Wastage(grms) :- " + str(self.wstge))
            
        def making_charges(self):
            self.mak_charges = self.mak_charges_per_grm*self.t_weight
            print("Making charges per gram :- " + str(self.mak_charges_per_grm))
            print("Total making charges :- " + str(self.mak_charges))
            
        def gst_charges(self):
            self.gst = self.gst_per*self.t_amount/100 
            print("GST charges :- " + str(self.gst))
            
        def total_amount(self):
            self.t_amount = self.p_gold*self.t_weight+self.mak_charges
            print("Total amount with out GST of " + self.need_item.title() + " is " + str(self.t_amount))
        
        def total_amount_gst(self):
            self.t_amount_gst = self.t_amount+self.gst
            print("Total amount with GST of " + self.need_item.title() + " is " + str(self.t_amount_gst))
            print("\n")
            
    my_orno = gold_ornament(input("enter gold ornament you want : "),
    int(input("enter today's market gold rate : ")),
    int(input("enter gold carat : ")),
    int(input("enter gold weight in grams : ")),
    int(input("enter wastage percentage : ")),
    int(input("enter making charges per gram : ")))

    my_orno.market_gold_rate()
    my_orno.carat()
    my_orno.weight()
    my_orno.wastage_percentage()
    my_orno.gold_price()
    my_orno.wastage()
    my_orno.total_weight()
    my_orno.making_charges()
    my_orno.total_amount()
    my_orno.gst_charges()
    my_orno.total_amount_gst()
    
elif condition == "s":
    
    class list_silver_ornaments():
        
        def __init__(self):
            self.silverornaments = []
            
        def list_s_ornaments(self):
            print("\nlist of silver ornaments available")
            for silverornament in self.silverornaments:
                print("- " + silverornament)
            print("\n") 
    my_list = list_silver_ornaments()
    my_list.silverornaments = ["patta golusu","mettelu","boddu golusu","utensils"]
    my_list.list_s_ornaments()
    
    class silver_ornaments():
        
        def __init__(self,ned_item,m_s_rate,wt_grms,ma_charges_per_grm):
            self.ned_item = ned_item
            self.to_amount = 0
            self.to_amount_gst = 0 
            self.m_s_rate = m_s_rate
            self.wt_grms = wt_grms
            self.ma_charges = 0
            self.ma_charges_per_grm = ma_charges_per_grm
            self.sgst_per = 3
            self.sgst = 0
               
        def mkt_silver_rate(self):
            print("\n\t***  Total bill details  ***\n")
            print("\nToday's market silver rate :- " + str(self.m_s_rate))

        def silver_weight(self):
            print("Weight(grms) :- " + str(self.wt_grms))
            
        def silver_making_charges(self):
            self.ma_charges = self.ma_charges_per_grm*self.wt_grms
            print("Total making charges :- " + str(self.ma_charges))
            
        def sgst_charges(self):
            self.sgst = self.sgst_per*self.to_amount/100 
            print("GST charges :- " + str(self.sgst))
            
        def s_total_amount(self):
            self.to_amount = self.m_s_rate*self.wt_grms+self.ma_charges
            print("Total amount with out GST of " + self.ned_item.title() + " is " + str(self.to_amount))
        
        def s_total_amount_gst(self):
            self.to_amount_gst = self.to_amount+self.sgst
            print("Total amount with GST of " + self.ned_item.title() + " is " + str(self.to_amount_gst)) 
            
    my_s_orno = silver_ornaments(input("enter silver ornament you want : "),
    int(input("enter today's market silver rate : ")),
    int(input("enter silver weight in grams : ")),
    float(input("enter making charges per gram : ")))
    my_s_orno.mkt_silver_rate()
    my_s_orno.silver_weight()
    my_s_orno.silver_making_charges()
    my_s_orno.s_total_amount()
    my_s_orno.sgst_charges()
    my_s_orno.s_total_amount_gst()

elif condition == "b":
    class list_gold_ornaments():
        
        def __init__(self):
            self.ornaments = []
            
        def list_g_ornaments(self):
            print("\nlist of gold ornaments available")
            for ornament in self.ornaments:
                print("- " + ornament)
            print("\n")  
    my_list = list_gold_ornaments()
    my_list.ornaments = ["Bangles","Chains","Earrings","Rings","Haaram","Necklaces",
                        "Ottiyanam","Pendant","Ruby & Emerald","Vanki"]
    my_list.list_g_ornaments()
    
    class list_silver_ornaments():
        
        def __init__(self):
            self.silverornaments = []
            
        def list_s_ornaments(self):
            print("\nlist of silver ornaments available")
            for silverornament in self.silverornaments:
                print("- " + silverornament)
            print("\n") 
    my_list = list_silver_ornaments()
    my_list.silverornaments = ["patta golusu","mettelu","boddu golusu","utensils"]
    my_list.list_s_ornaments()
    
    class gold_ornament():
    
        def __init__(self,need_item,m_g_rate,kt,w_grms,wstge_per,mak_charges_per_grm):
            self.need_item = need_item
            self.t_amount = 0
            self.t_amount_gst = 0 
            self.p_gold = 0
            self.m_g_rate = m_g_rate
            self.kt = kt
            self.w_grms = w_grms
            self.t_weight = 0
            self.wstge = 0
            self.wstge_per = wstge_per
            self.mak_charges = 0
            self.mak_charges_per_grm = mak_charges_per_grm
            self.gst_per = 3
            self.gst = 0
            self.sub_t_amount = 0
                
        
        def market_gold_rate(self):
            print("\n\t***  Total bill details for gold  ***\n")
            print("\nToday's market gold rate :- " + str(self.m_g_rate))
            
        def carat(self):
            print("Carat :- " + str(self.kt))   
                 
        def gold_price(self):
            self.p_gold = (self.kt/24)*self.m_g_rate
            print("\nGold price :- " + str(self.p_gold))
            
        def carat(self):
            print("Carat :- " + str(self.kt))
            
        def weight(self):
            print("Weight(grms) :- " + str(self.w_grms))
            
        def total_weight(self):
            self.t_weight = self.w_grms+self.wstge
            print("Total weight including wastage(grms) :- " + str(self.t_weight))
            
        def wastage_percentage(self):
            print("Wastage(%) :- " + str(self.wstge_per))
            
        def wastage(self):
            self.wstge = self.w_grms*self.wstge_per/100
            print("Wastage(grms) :- " + str(self.wstge))
            
        def making_charges(self):
            self.mak_charges = self.mak_charges_per_grm*self.t_weight
            print("Making charges per gram :- " + str(self.mak_charges_per_grm))
            print("Total making charges :- " + str(self.mak_charges))
            
        def gst_charges(self):
            self.gst = self.gst_per*self.t_amount/100 
            print("GST charges :- " + str(self.gst))
            
        def total_amount(self):
            self.t_amount = self.p_gold*self.t_weight+self.mak_charges
            print("Total amount with out GST of " + self.need_item.title() + " is " + str(self.t_amount))
        
        def total_amount_gst(self):
            self.t_amount_gst = self.t_amount+self.gst
            print("Total amount with GST of " + self.need_item.title() + " is " + str(self.t_amount_gst))
            print("\n")
    
    
    class silver_ornaments(gold_ornament):
        
        def __init__(self,need_item,m_g_rate,kt,w_grms,wstge_per,mak_charges_per_grm,ned_item,m_s_rate,wt_grms,ma_charges_per_grm):
            super().__init__(need_item,m_g_rate,kt,w_grms,wstge_per,mak_charges_per_grm)
            self.ned_item = ned_item
            self.to_amount = 0
            self.to_amount_gst = 0 
            self.m_s_rate = m_s_rate
            self.wt_grms = wt_grms
            self.ma_charges = 0
            self.ma_charges_per_grm = ma_charges_per_grm
            self.sgst_per = 3
            self.sgst = 0
            self.g_total = 0
               
        def mkt_silver_rate(self):
            print("\n\t***  Total bill details for silver  ***\n")
            print("\nToday's market silver rate :- " + str(self.m_s_rate))

        def silver_weight(self):
            print("Weight(grms) :- " + str(self.wt_grms))
            
        def silver_making_charges(self):
            self.ma_charges = self.ma_charges_per_grm*self.wt_grms
            print("Total making charges :- " + str(self.ma_charges))
            
        def sgst_charges(self):
            self.sgst = self.sgst_per*self.to_amount/100 
            print("GST charges :- " + str(self.sgst))
            
        def s_total_amount(self):
            self.to_amount = self.m_s_rate*self.wt_grms+self.ma_charges
            print("Total amount with out GST of " + self.ned_item.title() + " is " + str(self.to_amount))
        
        def s_total_amount_gst(self):
            self.to_amount_gst = self.to_amount+self.sgst
            print("Total amount with GST of " + self.ned_item.title() + " is " + str(self.to_amount_gst))
            
        def grand_total(self):
            self.g_total = self.to_amount_gst + self.t_amount_gst
            print("\n$ Total amount $ :- " + str(self.g_total))

    my_s_orno = silver_ornaments(input("enter gold ornament you want : "),
    int(input("enter today's market gold rate : ")),
    int(input("enter gold carat : ")),
    int(input("enter gold weight in grams : ")),
    int(input("enter wastage percentage : ")),
    int(input("enter making charges per gram : ")),input("\nenter silver ornament you want : "),
    int(input("enter today's market silver rate : ")),
    int(input("enter silver weight in grams : ")),
    float(input("enter making charges per gram : ")))
    
    my_s_orno.market_gold_rate()
    my_s_orno.carat()
    my_s_orno.weight()
    my_s_orno.wastage_percentage()
    my_s_orno.gold_price()
    my_s_orno.wastage()
    my_s_orno.total_weight()
    my_s_orno.making_charges()
    my_s_orno.total_amount()
    my_s_orno.gst_charges()
    my_s_orno.total_amount_gst()
    
    my_s_orno.mkt_silver_rate()
    my_s_orno.silver_weight()
    my_s_orno.silver_making_charges()
    my_s_orno.s_total_amount()
    my_s_orno.sgst_charges()
    my_s_orno.s_total_amount_gst()
    my_s_orno.grand_total()
    
    
