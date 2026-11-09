import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Bank

B = Bank('113.49.c.', 1004, own='hs_pfl.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

H('1.A',2,"Maya earns $40 a week. Which purchase is a need rather than a want?",
  "A winter coat when hers no longer fits",["A third pair of designer sneakers","A premium streaming bundle","A concert ticket"],"Needs are essentials such as clothing, food and shelter.")
H('1.A',2,"A shopper keeps asking, \"Do I need this or just want it?\" before buying. This habit helps with what?",
  "Evaluating spending decisions",["Raising credit scores","Avoiding all taxes","Increasing interest rates"],"Separating needs from wants prevents overspending.")
H('1.B',2,"A person who buys on impulse and rarely checks prices has which money tendency?",
  "A strong spending propensity",["A strong saving propensity","No money personality","A tax strategy"],"Money personality shows habits with spending and saving.")
H('1.B',2,"Why is it useful to know your own money personality?",
  "It helps you spot habits that may hurt or help your finances",["It sets your tax rate","It guarantees wealth","It fixes your credit score"],"Self-awareness guides better choices.")
H('1.C',2,"Donating to a food bank provides which benefit?",
  "It helps others in the community and may offer tax benefits",["It always earns interest","It raises your credit limit","It guarantees a refund"],"Charitable giving benefits both giver and community.")
H('1.C',2,"Which is an example of charitable giving?",
  "Volunteering time and donating money to a nonprofit",["Buying a lottery ticket","Paying rent","Opening a savings account"],"Giving can be money, goods or time.")
H('1.D',3,"Which financial goal is SMART (specific, measurable, attainable, relevant, time-bound)?",
  "Save $1,200 in 12 months by setting aside $100 each month",["Save a lot someday","Be rich","Spend less"],"SMART goals have numbers and deadlines.")
H('1.D',3,"A goal of paying for college in ten years is an example of which type of goal?",
  "A long-term goal",["A short-term goal","An impulse goal","A tax goal"],"Long-term goals take more than five years.")
H('2.A',3,"Reconciling a bank statement means doing what?",
  "Comparing it with your own records to confirm every deposit and withdrawal",["Closing the account","Paying a fee","Lowering the balance"],"It catches errors and fraud.")
H('2.A',3,"A reconciliation shows a $25 charge missing from your records. What should you do?",
  "Find out what it was and correct your records or dispute it",["Ignore it","Close the bank","Delete the statement"],"Unexplained charges need follow-up.")
H('2.B',3,"An income statement for a month lists what?",
  "Income received and expenses paid",["Only assets","Only loans","Only taxes owed"],"It shows inflows and outflows.")
H('2.B',3,"If monthly income is $2,400 and expenses are $2,150, what is the result?",
  "A surplus of $250",["A deficit of $250","A surplus of $2,150","Balanced at zero"],"Income minus expenses equals surplus or deficit.")
H('2.C',3,"A budget that includes short-, medium- and long-term goals should do what?",
  "Set aside money for each goal while covering essential expenses",["Ignore goals","Spend all income","Wait for a windfall"],"Budgets turn goals into monthly actions.")
H('2.C',3,"Which budget category would an emergency fund contribution belong to?",
  "Savings",["Entertainment","Transportation","Utilities"],"Emergency funds are savings.")
H('2.D',3,"Which is an asset?",
  "A car you own outright",["A credit card balance","A student loan","A past-due bill"],"Assets have value; liabilities are what you owe.")
H('2.D',3,"Which is a liability?",
  "A car loan balance",["Money in savings","A paid-off house","A retirement account"],"Liabilities are debts owed.")
H('2.E',3,"A net worth statement is calculated by doing what?",
  "Subtracting liabilities from assets",["Adding assets and liabilities","Subtracting income from expenses","Adding taxes to income"],"Net worth = assets - liabilities.")
H('2.E',3,"Assets of $18,000 and liabilities of $7,500 give a net worth of what?",
  "$10,500",["$25,500","$7,500","$18,000"],"18,000 - 7,500 = 10,500.")
H('2.F',3,"A $400 car repair that was not budgeted most likely does what?",
  "Reduces money available for other categories or goals",["Increases income","Raises net worth","Has no effect"],"Unplanned spending strains the budget.")
H('2.F',3,"Which strategy helps absorb unplanned spending?",
  "Maintaining an emergency fund",["Spending more","Skipping a budget","Paying only minimums"],"An emergency fund cushions surprises.")
H('3.A',3,"Which is an employee benefit?",
  "Employer-paid health insurance contributions",["Income tax","A parking ticket","Interest on a loan"],"Benefits add value beyond wages.")
H('3.A',3,"A 401(k) employer match is best described as what?",
  "Free money added to retirement savings when you contribute",["A tax","A fee","A loan"],"Matches boost retirement savings.")
H('3.B',3,"Which payroll tax funds Social Security and Medicare?",
  "FICA",["Sales tax","Property tax","Excise tax"],"The Federal Insurance Contributions Act tax is deducted from paychecks.")
H('3.B',3,"Which is usually deducted from a paycheck?",
  "Federal income tax",["Property tax","Sales tax","Tuition"],"Employers withhold income tax.")
H('3.C',3,"Gross pay is what?",
  "Total earnings before deductions",["Pay after taxes","Only overtime","Only bonuses"],"Net pay is gross minus deductions.")
H('3.C',3,"Gross pay is $1,000 and deductions are $230. Net pay is what?",
  "$770",["$1,230","$230","$700"],"1,000 - 230 = 770.")
H('4.A',3,"Which is a cost of owning a home that renters usually avoid?",
  "Property taxes and maintenance",["Monthly rent","Security deposit","Lease fee"],"Owners pay taxes, upkeep and repairs.")
H('4.A',3,"A benefit of owning a home compared with renting is what?",
  "Building equity as the loan is paid down",["No monthly payment","No repairs","No taxes"],"Equity is ownership value.")
H('4.B',3,"A benefit of leasing a vehicle rather than buying is what?",
  "Lower monthly payments, but no ownership at the end",["Unlimited mileage","Ownership after the term","No fees"],"Leases often have mileage limits and no equity.")
H('4.B',3,"Buying a car and keeping it for years is often cheaper in the long run because what?",
  "Payments end and you keep the vehicle",["Insurance is free","Gas is free","Repairs never occur"],"Ownership avoids repeated lease payments.")
H('4.C',3,"Rent-to-own arrangements usually cost more than paying cash because what?",
  "Total payments include high fees and markups",["The item is free","Interest is zero","There are no payments"],"Compare total cost, not just weekly payments.")
H('4.C',3,"Which payment method usually has the highest total cost for the same item?",
  "Store credit with a high interest rate carried for months",["Paying cash","Saving first","Using a debit card"],"Interest increases total cost.")
H('4.D',3,"Which strategy helps a consumer make a smart purchase?",
  "Comparing unit prices and reading reviews",["Buying the first option","Following a slogan","Skipping research"],"Informed buying saves money.")
H('4.D',3,"A 12-ounce box costs $3.00 and a 20-ounce box costs $4.60. Which is the better unit price?",
  "The 20-ounce box at $0.23 per ounce",["The 12-ounce box at $0.25 per ounce","They are equal","The 12-ounce box at $0.20 per ounce"],"4.60 / 20 = 0.23; 3.00 / 12 = 0.25.")
H('5.A',3,"A good short-term saving goal is to do what?",
  "Build an emergency fund covering several months of expenses",["Buy a house now","Invest everything in one stock","Spend savings on wants"],"Emergency funds protect against surprises.")
H('5.A',3,"Where is an emergency fund best kept?",
  "In an easily accessible savings account",["Locked in a long-term fund","In a risky stock","Under a mattress only"],"Liquidity matters for emergencies.")
H('5.B',3,"Saving for a house down payment in five years is an example of what?",
  "Intermediate-term saving and investing",["Short-term saving","Retirement saving only","Spending"],"Goals of several years are intermediate-term.")
H('5.B',3,"For a goal five years away, a moderate mix of savings and lower-risk investments is common because what?",
  "There is time to earn returns but limited time to recover from losses",["Risk is irrelevant","Money cannot grow","Taxes are zero"],"Time horizon affects risk.")
H('5.C',3,"A charitable contribution to a qualified nonprofit may do what on a tax return?",
  "Reduce taxable income if deductions are itemized",["Increase the tax owed","Cancel all taxes","Raise income"],"Charitable deductions can lower tax.")
H('5.C',3,"To claim a charitable deduction, a donor should keep what?",
  "Receipts or acknowledgment letters",["Nothing","Only a verbal note","Social media posts"],"Records support deductions.")
H('5.D',3,"A long-term investing strategy for retirement should emphasize what?",
  "Consistent contributions over many years",["Waiting until age 60","Spending savings","Avoiding investing"],"Time and consistency build wealth.")
H('5.D',3,"Which account type offers tax advantages for retirement saving?",
  "401(k) or IRA",["Checking account","Credit card","Payday loan"],"Retirement accounts provide tax benefits.")
H('6.A',3,"Banks and credit unions help savers by doing what?",
  "Holding deposits safely and paying interest",["Taking money without return","Setting taxes","Selling insurance only"],"Financial institutions channel savings to borrowers.")
H('6.A',3,"The stock market allows investors to do what?",
  "Buy and sell ownership shares in companies",["Print money","Set interest rates","Collect taxes"],"Markets connect investors and companies.")
H('6.B',3,"Compound growth means that interest is earned on what?",
  "Both the original deposit and previously earned interest",["Only the original deposit","Only the interest","Neither"],"Growth accelerates over time.")
H('6.B',3,"$1,000 grows at 5 percent compounded annually. After one year the balance is $1,050. After the second year it is closest to what?",
  "$1,102.50",["$1,100.00","$1,050.00","$1,200.00"],"1,050 x 1.05 = 1,102.50.")
H('6.C',3,"A certificate of deposit (CD) typically does what?",
  "Pays a fixed rate if you leave the money for a set term",["Allows unlimited free withdrawals","Has no risk of penalty","Pays variable stock returns"],"Early withdrawal usually incurs a penalty.")
H('6.C',3,"Compared with a checking account, a savings account usually offers what?",
  "Higher interest but limits on withdrawals",["No interest","Unlimited checks","Higher fees"],"Savings are for accumulating money.")
H('6.D',3,"Stocks generally offer which risk-return trade-off compared with bonds?",
  "Higher potential return with greater risk",["Lower return with greater risk","Guaranteed return","No risk"],"Risk and return are related.")
H('6.D',3,"A mutual fund helps investors by doing what?",
  "Pooling money to buy a diversified mix of investments",["Guaranteeing profit","Eliminating all risk","Setting taxes"],"Diversification spreads risk.")
H('7.A',3,"Which is a cost people face in retirement?",
  "Health care and possible long-term care",["Payroll tax on wages","Child care for toddlers","School tuition only"],"Medical costs rise with age.")
H('7.A',3,"Many retirees need money for which basic expense?",
  "Housing and daily living costs",["No expenses","Only entertainment","Only taxes"],"Living costs continue in retirement.")
H('7.B',3,"Which is a common source of retirement income?",
  "Social Security benefits",["A student loan","A payday loan","A credit card"],"Social Security replaces part of earnings.")
H('7.B',3,"A pension is best described as what?",
  "A regular payment from an employer plan after retirement",["A tax refund","A student grant","A credit line"],"Pensions pay retirees.")
H('7.C',3,"Starting to save for retirement at 25 instead of 45 helps because of what?",
  "Compound growth has more years to work",["Taxes are lower","Prices are lower","Interest is fixed"],"Time magnifies growth.")
H('7.C',3,"Saving a sufficient percentage of income each year matters because what?",
  "Small amounts may not fund retirement needs",["Savings are taxed away","Social Security covers everything","Retirement is short"],"Adequate savings are required.")
H('8.A',3,"Which source of credit is generally the most expensive?",
  "A payday loan",["A bank loan","A credit union loan","A student loan"],"Payday loans have very high APRs.")
H('8.A',3,"A title loan requires a borrower to do what?",
  "Use a vehicle title as collateral",["Provide no security","Pay no interest","Skip repayment"],"Failure to repay can mean losing the vehicle.")
H('8.B',3,"Revolving credit, such as a credit card, allows a borrower to do what?",
  "Borrow repeatedly up to a limit",["Borrow once only","Avoid payments","Skip interest"],"Balances can be reused.")
H('8.B',3,"An auto loan with equal monthly payments for 60 months is what type of credit?",
  "Installment credit",["Revolving credit","Unsecured credit","Charge card"],"Installment loans have fixed payments.")
H('8.C',3,"Taking on a $350 monthly loan payment affects a budget by doing what?",
  "Reducing the money available for other expenses and goals",["Increasing income","Raising net worth immediately","Having no effect"],"Debt payments are a fixed expense.")
H('8.C',3,"Borrowing to buy a depreciating item can do what to net worth?",
  "Lower it, because liabilities may exceed asset value",["Raise it","Have no effect","Double it"],"Debt rises while value falls.")
H('9.A',3,"Which of the three Cs of credit refers to a borrower's reliability and history of repaying?",
  "Character",["Capacity","Collateral","Capital"],"Lenders consider character, capacity and collateral.")
H('9.A',3,"Capacity in credit evaluation means what?",
  "The borrower's ability to repay from income",["The size of the bank","The interest rate","The loan term"],"Income relative to debts matters.")
H('9.B',3,"Consumers can get a free credit report from the three major credit bureaus at what site?",
  "AnnualCreditReport.com",["Any shopping website","A social media app","A ticket seller"],"The official site is annualcreditreport.com.")
H('9.B',3,"A credit score is best described as what?",
  "A number summarizing how risky a borrower appears",["A tax rate","A bank balance","A salary"],"Higher scores mean lower risk.")
H('9.C',3,"Why check credit reports regularly?",
  "To catch errors and signs of identity theft",["To raise interest rates","To avoid taxes","To close accounts"],"Mistakes can lower scores.")
H('9.C',3,"If you find an error on a credit report, you should do what?",
  "Dispute it with the credit bureau in writing",["Ignore it","Pay a stranger","Close all accounts"],"Disputes can correct errors.")
H('9.D',3,"Which event could lead to bankruptcy?",
  "Large unpaid medical bills after job loss",["A raise","A tax refund","A savings deposit"],"Unexpected hardship plus debt can overwhelm a household.")
H('9.D',3,"Bankruptcy is a legal process in which what happens?",
  "A person seeks relief from debts they cannot repay",["A person pays no taxes","A bank closes","Credit is improved"],"It has long-term credit consequences.")
H('9.E',3,"Paying bills 30 days late repeatedly will most likely do what?",
  "Lower your credit score",["Raise it","Remove debt","Improve rates"],"Payment history is a key factor.")
H('9.E',3,"A consequence of poor credit management can be what?",
  "Higher interest rates and difficulty renting or getting loans",["Lower interest rates","Instant approvals","Free credit"],"Poor credit raises costs.")
H('10.A',3,"APR stands for what?",
  "Annual percentage rate",["Annual payment return","Average price range","Applied profit ratio"],"APR expresses yearly borrowing cost.")
H('10.A',3,"A fixed interest rate on a loan does what?",
  "Stays the same for the life of the loan",["Changes monthly","Rises with the market","Disappears"],"A variable rate can change.")
H('10.B',3,"A larger down payment reduces the total cost of borrowing because what?",
  "Less money is borrowed, so less interest accrues",["Interest is higher","The loan term is longer","Fees double"],"Principal is smaller.")
H('10.B',3,"Making extra payments toward principal helps by doing what?",
  "Reducing interest costs and paying off the loan sooner",["Increasing interest","Extending the term","Adding fees"],"Extra principal payments save money.")
H('10.C',3,"A debit card differs from a credit card in that a debit card does what?",
  "Withdraws money directly from your bank account",["Borrows from the bank","Charges interest monthly","Builds credit by itself"],"Debit uses your own funds.")
H('10.C',3,"Carrying a balance on a credit card leads to what?",
  "Interest charges added to what you owe",["Free money","Lower balance automatically","No cost"],"Paying in full avoids interest.")
H('11.A',3,"Financial risk can be defined as what?",
  "The possible loss of assets or earning potential",["A guaranteed gain","A tax benefit","An interest rate"],"Risk involves chance of loss.")
H('11.A',3,"Which event is a financial risk?",
  "Losing a job",["Getting a raise","Winning a prize","Earning interest"],"Job loss reduces earning potential.")
H('11.B',3,"Buying insurance to protect against a major loss is an example of which risk strategy?",
  "Transferring risk",["Avoiding risk","Retaining risk","Ignoring risk"],"The insurer takes on the risk.")
H('11.B',3,"Choosing not to take a dangerous activity is what risk strategy?",
  "Avoiding risk",["Transferring risk","Retaining risk","Reducing risk"],"Avoidance eliminates exposure.")
H('12.A',3,"Dana pays $120 every month to keep her auto policy active. What is that payment called?",
  "A premium",["A deductible","A co-pay","A policy limit"],"A deductible is the amount you pay before coverage.")
H('12.A',3,"A policy has a $500 deductible and a $10,000 policy limit. What does the $10,000 represent?",
  "The maximum amount the insurer will pay for a covered loss",["The amount paid before coverage starts","The monthly payment","A fixed fee per visit"],"Higher deductibles often mean lower premiums.")
H('12.B',3,"Employer-sponsored health insurance often costs less than individual coverage because what?",
  "Employers usually share part of the premium",["There are no premiums","Coverage is free","Deductibles are zero"],"Employers subsidize group plans.")
H('12.B',3,"A co-pay is what?",
  "A fixed fee you pay for a covered service",["The annual premium","A tax","The total bill"],"For example, $30 per doctor visit.")
H('12.C',3,"Disability insurance protects against what?",
  "Loss of income if you cannot work due to illness or injury",["Car repairs","Home theft","Tax bills"],"It replaces part of earnings.")
H('12.C',3,"Long-term care insurance helps pay for what?",
  "Extended care such as nursing homes or in-home help",["Groceries","College","Vacations"],"It covers costs not covered by regular health insurance.")
H('12.D',3,"Term life insurance differs from whole life insurance in that term insurance does what?",
  "Covers a set period and usually costs less",["Never expires","Builds cash value","Costs more"],"Whole life builds cash value.")
H('12.D',3,"Life insurance is most important for people who do what?",
  "Have dependents who rely on their income",["Have no dependents","Own no property","Are retired with no obligations"],"It protects survivors.")
H('12.E',3,"Renter's insurance generally covers what?",
  "The renter's belongings and liability",["The building structure","The landlord's income","Rent payments"],"The landlord insures the building.")
H('12.E',3,"Homeowner's insurance generally covers what?",
  "Damage to the home and personal property from covered events",["Mortgage interest","Property taxes","Utilities"],"Policies list covered perils.")
H('12.F',3,"Which factor can raise the price of automobile insurance?",
  "A history of accidents or tickets",["A clean record","Safe driving courses","Few miles driven"],"Risk drives prices.")
H('12.F',3,"Liability coverage in auto insurance pays for what?",
  "Damage or injuries you cause to others",["Your own car repairs","Gas","Tires"],"Liability is required in Texas.")
H('12.G',3,"An extended warranty is best described as what?",
  "Optional coverage that may not be worth its cost",["A required item","A tax","A free service"],"Compare the cost with likely repairs.")
H('12.G',3,"Mortgage insurance is usually required when a buyer does what?",
  "Makes a small down payment",["Pays in cash","Buys a condo only","Rents"],"It protects the lender.")
H('13.A',3,"Which action helps prevent identity theft?",
  "Shredding documents with personal information",["Sharing your PIN","Using one password everywhere","Posting your Social Security number"],"Protect personal data.")
H('13.A',3,"A strong password is one that does what?",
  "Is long, unique and hard to guess",["Is your birthday","Is the same everywhere","Is short"],"Use unique passwords.")
H('13.B',3,"An email that urges you to click a link and confirm your bank password is most likely what?",
  "A phishing scam",["A tax refund","A free gift","A bank statement"],"Phishing tricks people into giving information.")
H('13.B',3,"A pyramid scheme earns money mainly by doing what?",
  "Recruiting new participants who pay in",["Selling real products","Investing in stocks","Paying taxes"],"It collapses when recruitment stops.")
H('13.C',3,"The Better Business Bureau helps consumers by doing what?",
  "Providing business ratings and handling complaints",["Setting interest rates","Collecting taxes","Printing money"],"Consumer protection agencies help resolve disputes.")
H('13.C',3,"Which agency regulates consumer financial products like credit cards and mortgages?",
  "The Consumer Financial Protection Bureau",["The Post Office","The NFL","The Weather Service"],"The CFPB protects consumers.")
H('14.A',3,"A will is a legal document that does what?",
  "Directs how your property is distributed after death",["Appoints a doctor","Sets taxes","Pays bills"],"Wills also name guardians for minor children.")
H('14.A',3,"A beneficiary designation on a retirement account does what?",
  "Names who receives the account after the owner dies",["Names the bank","Sets the interest","Lists the fees"],"Designations usually override wills.")
H('14.B',3,"A power of attorney allows someone to do what?",
  "Act on your behalf in legal or financial matters",["Receive your paycheck","Vote for you","Write your will"],"You choose a trusted agent.")
H('14.B',3,"A living will states what?",
  "Your wishes for medical treatment if you cannot speak for yourself",["Where your property goes","Your tax return","Your funeral costs"],"It guides end-of-life care.")
H('15.A',3,"On average, higher levels of education are associated with what?",
  "Higher earnings and lower unemployment",["Lower earnings","No difference","Higher debt only"],"Education generally boosts earnings.")
H('15.A',3,"A worker with a bachelor's degree typically earns what compared with one with only a high school diploma?",
  "More, on average",["Less","The same always","Nothing"],"Earnings rise with education.")
H('15.B',3,"Which is a direct cost of college?",
  "Tuition and fees",["Wages earned","Scholarships received","Tax refunds"],"Costs include books, housing and food.")
H('15.B',3,"Opportunity cost of attending college full time includes what?",
  "Income you could have earned by working",["Free tuition","Grants","Interest"],"Foregone wages are a real cost.")
H('15.C',3,"Which type of institution usually has the lowest tuition for in-state students?",
  "Public community college",["Private university","Elite private college","For-profit school with high fees"],"Public two-year schools are lower cost.")
H('15.C',3,"Why may a private university cost more than a public one?",
  "It receives less state funding and relies more on tuition",["It pays no staff","It has no buildings","It charges nothing"],"Public schools receive state support.")
H('15.D',3,"Which measure helps evaluate the quality of a college investment?",
  "Graduation rate and job placement outcomes",["Color of the logo","Mascot","Campus slogan"],"Outcomes show value.")
H('15.D',3,"A school with a very low graduation rate and high debt for students is likely to be what?",
  "A poor educational investment",["An excellent investment","Free","Risk free"],"Evaluate cost against outcomes.")
H('16.A',3,"The FAFSA is used to apply for what?",
  "Federal student aid",["A mortgage","A credit card","A car loan"],"It determines eligibility for grants, loans and work-study.")
H('16.A',3,"When is it best to submit the FAFSA?",
  "As early as possible after it opens",["After graduation","Only at the deadline","Never"],"Some aid is limited and first-come.")
H('16.B',3,"Which is a source of funds for college that does not need to be repaid?",
  "A scholarship",["A student loan","A credit card","A payday loan"],"Scholarships and grants are gifts.")
H('16.B',3,"Work-study programs help students by doing what?",
  "Providing part-time jobs to earn money for school",["Giving free tuition","Forgiving loans","Paying taxes"],"Students earn wages.")
H('16.C',3,"A disadvantage of student loans is that they must be what?",
  "Repaid with interest",["Forgotten","Ignored","Forgiven automatically"],"Debt affects future income.")
H('16.C',3,"An advantage of grants over loans is that grants do what?",
  "Do not have to be repaid",["Must be repaid","Have interest","Require collateral"],"Grants reduce borrowing.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_pfl.jsonl'))
