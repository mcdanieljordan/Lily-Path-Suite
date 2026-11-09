insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_pfle_v1'
from (values
('113.76.d.1.A',3,'A student chooses to work a shift instead of going to a ballgame. What is the opportunity cost of working?','["the enjoyment of the ballgame", "the wages earned", "nothing at all", "the cost of gas"]'::jsonb,0,'Opportunity cost is the next best alternative given up.','original'),
('113.76.d.1.A',3,'Scarcity exists because what?','["prices never change", "people''s wants are unlimited but resources are limited", "money is free", "there is too much of everything"]'::jsonb,1,'Scarcity forces choices.','original'),
('113.76.d.1.B',3,'On a production-possibilities curve, a point inside the curve shows what?','["prices are rising", "the economy is at maximum output", "resources are not fully or efficiently used", "output is impossible"]'::jsonb,2,'Points on the curve are efficient; inside is underuse.','original'),
('113.76.d.1.B',3,'A point outside a production-possibilities curve is what?','["wasteful", "efficient", "already achieved", "unattainable with current resources and technology"]'::jsonb,3,'Growth could make it attainable later.','original'),
('113.76.d.1.C',3,'Moving along a production-possibilities curve to make more of one good shows what?','["a trade-off, because less of another good is made", "unlimited resources", "a price decrease", "no cost"]'::jsonb,0,'Each choice has a cost.','original'),
('113.76.d.1.D',3,'In the circular flow model, households provide firms with what?','["finished goods", "resources such as labor", "tax revenue", "patents"]'::jsonb,1,'Households sell resources to firms in exchange for income.','original'),
('113.76.d.1.D',3,'In the circular flow model, firms pay households for resources with what?','["products", "taxes", "wages, rent and interest", "tariffs"]'::jsonb,2,'Payments become household income.','original'),
('113.76.d.1.E',3,'According to the law of demand, when the price of a good rises, what usually happens?','["the quantity demanded rises", "demand becomes zero", "supply disappears", "the quantity demanded falls"]'::jsonb,3,'Higher prices reduce purchases.','original'),
('113.76.d.1.E',3,'According to the law of supply, when the price of a good rises, producers usually do what?','["supply more", "lower costs", "supply less", "stop selling"]'::jsonb,0,'Higher prices raise profit incentive.','original'),
('113.76.d.1.F',3,'On a supply-and-demand graph, the equilibrium point is where what?','["the axes meet", "supply and demand curves intersect", "demand is zero", "supply is zero"]'::jsonb,1,'At equilibrium the market clears.','original'),
('113.76.d.1.F',3,'If the price is above equilibrium, what results?','["a shortage", "inflation only", "a surplus", "balance"]'::jsonb,2,'Quantity supplied exceeds quantity demanded.','original'),
('113.76.d.1.F',3,'If the price is below equilibrium, what results?','["a surplus", "deflation only", "balance", "a shortage"]'::jsonb,3,'Quantity demanded exceeds quantity supplied.','original'),
('113.76.d.1.G',3,'A change in consumer income or tastes is an example of what?','["a non-price determinant of demand", "a tariff", "a price ceiling", "a determinant of supply"]'::jsonb,0,'These shift the demand curve.','original'),
('113.76.d.1.G',3,'A new technology that lowers production costs will most likely do what to supply?','["make it vertical", "increase it", "have no effect", "decrease it"]'::jsonb,1,'Lower costs shift the supply curve right.','original'),
('113.76.d.1.H',3,'In a resource market, who is the seller?','["banks", "the government", "households", "firms"]'::jsonb,2,'Households sell labor and land to firms.','original'),
('113.76.d.1.H',3,'In a product market, who is the buyer?','["the Federal Reserve", "banks only", "firms", "households"]'::jsonb,3,'Households buy goods and services.','original'),
('113.76.d.2.A',3,'A progressive tax is one in which what happens?','["higher incomes pay a higher percentage", "no one pays", "lower incomes pay a higher percentage", "everyone pays the same percentage"]'::jsonb,0,'The federal income tax is progressive.','original'),
('113.76.d.2.A',3,'A regressive tax takes a larger share from whom?','["no one", "lower-income people", "higher-income people", "corporations only"]'::jsonb,1,'Sales taxes can be regressive.','original'),
('113.76.d.2.B',3,'Social Security taxes (FICA) pay for what?','["public schools", "highways", "retirement, survivor and disability benefits", "defense only"]'::jsonb,2,'Workers and employers both contribute.','original'),
('113.76.d.2.B',3,'Which tax is paid mostly by local governments from property owners?','["tariff", "income tax", "payroll tax", "property tax"]'::jsonb,3,'Local schools rely on it.','original'),
('113.76.d.2.C',3,'All real-world economies are what?','["mixed, with both market and government roles", "pure market only", "pure command only", "traditional only"]'::jsonb,0,'They lie on a spectrum.','original'),
('113.76.d.2.D',3,'Which is a benefit of the U.S. free enterprise system?','["no competition", "private property and the profit motive", "price controls on everything", "government ownership of all firms"]'::jsonb,1,'Incentives encourage innovation.','original'),
('113.76.d.2.D',3,'Competition in free enterprise helps consumers because it does what?','["eliminates quality", "raises all prices", "pushes firms toward lower prices and better products", "ends choice"]'::jsonb,2,'Firms compete for customers.','original'),
('113.76.d.2.E',3,'A goal of full employment means what?','["prices rise quickly", "no one works", "wages are zero", "most people who want jobs can find them"]'::jsonb,3,'Some frictional unemployment remains.','original'),
('113.76.d.2.E',3,'Price stability means what?','["keeping inflation low and predictable", "prices always rise", "prices never change", "prices fall rapidly"]'::jsonb,0,'Stable prices help planning.','original'),
('113.76.d.2.F',3,'Lowering taxes and raising government spending to boost a weak economy is what kind of policy?','["monetary policy", "expansionary fiscal policy", "tariff policy", "contractionary fiscal policy"]'::jsonb,1,'It aims to raise demand.','original'),
('113.76.d.2.G',3,'When the Federal Reserve raises interest rates, borrowing becomes what?','["illegal", "free", "more expensive", "cheaper"]'::jsonb,2,'Higher rates slow spending and inflation.','original'),
('113.76.d.2.G',3,'The Federal Reserve is the nation''s what?','["stock exchange", "insurance company", "tax collector", "central bank"]'::jsonb,3,'It manages money supply and interest rates.','original'),
('113.76.d.3.A',3,'On average, how does education level relate to earnings?','["more education usually means higher lifetime earnings", "more education always means lower pay", "education has no relation", "only experience matters"]'::jsonb,0,'Earnings rise with education on average.','original'),
('113.76.d.3.A',3,'Unemployment rates are generally what for workers with more education?','["higher", "lower", "the same", "not tracked"]'::jsonb,1,'Education improves job security.','original'),
('113.76.d.3.B',3,'Which cost should be compared when choosing a postsecondary option?','["only the weather", "only the distance", "tuition, fees, living costs and expected earnings", "only the mascot"]'::jsonb,2,'Weigh costs and benefits.','original'),
('113.76.d.3.B',3,'A typical benefit of a technical or trade program is what?','["no classes", "a guaranteed job", "no cost ever", "preparing for a skilled job in a shorter time"]'::jsonb,3,'Programs vary in length and cost.','original'),
('113.76.d.3.C',3,'The FAFSA is used to apply for what?','["federal student aid", "a driver''s license", "a passport", "a mortgage"]'::jsonb,0,'It is the Free Application for Federal Student Aid.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_pfle_v1'
from (values
('113.76.d.3.C',3,'Scholarships differ from loans because scholarships do what?','["must be repaid with interest", "do not have to be repaid", "are only for adults", "are only for loans"]'::jsonb,1,'Scholarships are gift aid.','original'),
('113.76.d.3.D',3,'Compared with private loans, federal student loans often offer what?','["variable terms only", "no repayment", "income-driven repayment options and borrower protections", "higher fees always"]'::jsonb,2,'Federal loans have standardized protections.','original'),
('113.76.d.3.D',3,'A grant is financial aid that does what?','["must be repaid at once", "is a loan with high interest", "is a type of credit card", "does not need to be repaid"]'::jsonb,3,'Pell Grants are need-based.','original'),
('113.76.d.3.E',3,'A Student Aid Report (SAR) summarizes what?','["the information from a FAFSA and the expected family contribution", "a credit score", "a bank balance", "a student''s grades"]'::jsonb,0,'It helps colleges determine aid.','original'),
('113.76.d.3.F',3,'To align careers with interests, a student should do what?','["pick randomly", "research jobs, required training and earnings", "avoid planning", "ignore skills"]'::jsonb,1,'Match interests to opportunities.','original'),
('113.76.d.4.A',3,'Interest earned on a savings account is a source of what?','["a tax deduction only", "debt", "income", "insurance"]'::jsonb,2,'Income also includes wages, profits and rent.','original'),
('113.76.d.4.A',3,'Money earned by a worker for hours worked is called what?','["dividends", "rent", "profit", "wages"]'::jsonb,3,'Wages are payment for labor.','original'),
('113.76.d.4.B',3,'Which of these is a common employee benefit?','["employer-provided health insurance", "free housing", "unlimited vacation", "a free car for everyone"]'::jsonb,0,'Benefits add to total compensation.','original'),
('113.76.d.4.B',3,'A 401(k) is what kind of benefit?','["a loan", "a retirement savings plan", "a health plan", "a tax refund"]'::jsonb,1,'Employers often match contributions.','original'),
('113.76.d.4.C',3,'A worker earns $1,000 gross pay and has $200 withheld for taxes and deductions. What is the net pay?','["$1,200", "$200", "$800", "$1,000"]'::jsonb,2,'Net pay = gross - deductions.','original'),
('113.76.d.4.C',3,'Gross income is what?','["only tips", "income after taxes", "only bonus pay", "total income before taxes and deductions"]'::jsonb,3,'Net is what you take home.','original'),
('113.76.d.4.D',3,'Which factor is likely to raise pay in a career?','["high demand for the skill", "a lack of training", "many available workers", "low qualifications"]'::jsonb,0,'Scarce skills pay more.','original'),
('113.76.d.5.A',3,'An entrepreneur is a person who does what?','["inherits a business", "starts and manages a business taking financial risk", "works only for wages", "owns only stocks"]'::jsonb,1,'Entrepreneurs create new ventures.','original'),
('113.76.d.5.B',3,'An entrepreneur earns profit when what?','["costs are greater than revenue", "sales are zero", "revenue is greater than costs", "taxes are zero"]'::jsonb,2,'Profit = revenue - cost.','original'),
('113.76.d.5.C',3,'A self-employed person usually must do what that an employee does not?','["get paid sick leave", "receive employer benefits automatically", "avoid taxes", "pay both halves of Social Security and Medicare taxes"]'::jsonb,3,'Self-employed workers pay self-employment tax.','original'),
('113.76.d.5.D',3,'The Small Business Administration (SBA) helps entrepreneurs by doing what?','["offering loans, guidance and training", "owning small businesses", "collecting income taxes", "setting prices"]'::jsonb,0,'Government and other agencies support startups.','original'),
('113.76.d.5.E',3,'A major risk of starting a business is what?','["guaranteed profit", "losing the money invested", "no competition", "no workload"]'::jsonb,1,'Reward and risk go together.','original'),
('113.76.d.5.E',3,'A reward of entrepreneurship is the possibility of what?','["guaranteed income", "avoiding all risk", "earning profits and being your own boss", "no responsibilities"]'::jsonb,2,'Rewards balance risk.','original'),
('113.76.d.5.F',3,'In a sole proprietorship, the owner has what?','["shareholders", "limited liability", "no taxes", "unlimited personal liability for debts"]'::jsonb,3,'One owner is personally responsible.','original'),
('113.76.d.5.F',3,'A corporation is a business that is what?','["a separate legal entity owned by shareholders", "a government agency", "owned by one person personally", "always tax-free"]'::jsonb,0,'Shareholders have limited liability.','original'),
('113.76.d.5.F',3,'In a partnership, what do owners share?','["nothing", "profits, losses and responsibilities", "only profits", "only losses"]'::jsonb,1,'Partnerships have two or more owners.','original'),
('113.76.d.6.A',3,'A SMART financial goal is one that is what?','["vague and flexible", "endless", "specific, measurable, attainable, relevant and time-bound", "secret"]'::jsonb,2,'Good goals have clear targets.','original'),
('113.76.d.6.A',3,'Saving for a trip next year is what kind of goal?','["a long-term goal", "a retirement goal", "an unattainable goal", "a short-term goal"]'::jsonb,3,'Short-term goals are within about a year.','original'),
('113.76.d.6.B',3,'The opportunity cost of spending $50 on a game now is what?','["what else the $50 could have bought or earned in savings", "the sales tax only", "nothing", "the price of the game"]'::jsonb,0,'Spending today reduces saving.','original'),
('113.76.d.6.C',3,'Prioritizing purchases means doing what?','["buying everything", "deciding needs before wants", "buying wants first", "avoiding all purchases"]'::jsonb,1,'Needs come first.','original'),
('113.76.d.6.C',3,'Charitable giving is what?','["paying taxes", "taking out a loan", "donating money or time to support a cause", "buying luxuries"]'::jsonb,2,'Giving can be part of a budget.','original'),
('113.76.d.6.D',3,'One advantage of a debit card over a credit card is that it does what?','["charges interest", "builds credit history", "has a grace period", "spends your own money rather than borrowing"]'::jsonb,3,'A debit card draws directly from a checking account.','original'),
('113.76.d.6.D',3,'Which form of payment can lead to interest charges if not paid in full?','["a credit card", "a debit card", "a money order", "cash"]'::jsonb,0,'Balances carry interest.','original'),
('113.76.d.6.E',3,'Tracking income and expenses helps a person do what?','["raise prices", "see where money goes and reconcile accounts", "avoid all taxes", "ignore bills"]'::jsonb,1,'Records support good decisions.','original'),
('113.76.d.6.E',3,'Reconciling a bank statement means doing what?','["paying taxes", "closing the account", "comparing your records to the bank''s records", "borrowing money"]'::jsonb,2,'It finds errors or fraud.','original'),
('113.76.d.6.F',3,'An unplanned expense such as a car repair can do what to a budget?','["be avoided always", "have no effect", "increase income automatically", "force cuts elsewhere or the use of savings"]'::jsonb,3,'Emergency funds help absorb surprises.','original'),
('113.76.d.6.G',3,'A benefit of renting rather than owning is what?','["lower upfront cost and no repair responsibility", "building equity", "tax deductions for interest", "no monthly payments"]'::jsonb,0,'Owning builds equity but costs more upfront.','original'),
('113.76.d.6.G',3,'A benefit of owning a home is what?','["no taxes", "building equity as the loan is paid down", "no maintenance", "no risk"]'::jsonb,1,'Owners also pay property taxes and repairs.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_pfle_v1'
from (values
('113.76.d.6.H',3,'A benefit of leasing a vehicle is often what?','["owning the car at the end", "no fees", "lower monthly payments", "no mileage limits"]'::jsonb,2,'But you have no equity.','original'),
('113.76.d.6.H',3,'A drawback of leasing a car is what?','["higher upfront cost than buying always", "no insurance", "no payments", "mileage limits and no ownership at the end"]'::jsonb,3,'Leases have restrictions.','original'),
('113.76.d.7.A',3,'Which is a source of credit?','["a bank or credit union", "a coupon", "a savings goal", "a paycheck"]'::jsonb,0,'Credit means borrowing.','original'),
('113.76.d.7.A',3,'Peer-to-peer lending connects what?','["firms with the Fed", "individual borrowers with individual lenders online", "governments with citizens", "banks with banks"]'::jsonb,1,'It is a newer source of credit.','original'),
('113.76.d.7.B',3,'A payday loan is an example of what risky practice?','["safe borrowing", "a savings account", "predatory lending with very high fees and interest", "a government grant"]'::jsonb,2,'Predatory lenders target vulnerable borrowers.','original'),
('113.76.d.7.B',3,'A sign of predatory lending is what?','["no fees", "clear terms", "low fixed rates", "extremely high interest rates and hidden fees"]'::jsonb,3,'Read the terms carefully.','original'),
('113.76.d.7.C',3,'A credit card is an example of what kind of credit?','["revolving credit", "a scholarship", "installment credit", "a grant"]'::jsonb,0,'You can borrow repeatedly up to a limit.','original'),
('113.76.d.7.C',3,'A car loan with fixed monthly payments is what kind of credit?','["a rebate", "installment credit", "a grant", "revolving credit"]'::jsonb,1,'Installment loans have a fixed schedule.','original'),
('113.76.d.7.D',3,'The three Cs of credit are what?','["cars, cards and cash", "cost, charge and credit", "character, capacity and collateral", "cash, checks and coins"]'::jsonb,2,'Lenders evaluate these when deciding.','original'),
('113.76.d.7.D',3,'''Collateral'' is what?','["interest on a loan", "a late fee", "a credit score", "property pledged to secure a loan"]'::jsonb,3,'Lenders can claim it if you default.','original'),
('113.76.d.7.E',3,'Consumers can get free credit reports from which website?','["AnnualCreditReport.com", "a bank''s ads", "a store coupon site", "a random email link"]'::jsonb,0,'Federal law allows free reports.','original'),
('113.76.d.7.E',3,'A credit score is a number that does what?','["sets tax rates", "estimates how likely you are to repay debt", "shows your net worth", "measures your income"]'::jsonb,1,'Higher scores usually get lower interest rates.','original'),
('113.76.d.7.F',3,'Why should you check your credit report regularly?','["to avoid bills", "to raise your income", "to find errors or signs of identity theft", "to lower taxes"]'::jsonb,2,'Errors can hurt your score.','original'),
('113.76.d.7.G',3,'A job loss or medical expense can affect credit by doing what?','["preventing late fees", "raising your score automatically", "erasing debts", "making it harder to pay debts on time"]'::jsonb,3,'Financial shocks can cause missed payments.','original'),
('113.76.d.7.H',3,'The Truth in Lending Act requires lenders to disclose what?','["the cost of credit including the APR", "your taxes", "your salary", "your credit score"]'::jsonb,0,'It helps consumers compare loans.','original'),
('113.76.d.7.H',3,'Annual percentage rate (APR) shows what?','["the number of payments", "the yearly cost of borrowing as a percentage", "the credit limit", "the loan balance"]'::jsonb,1,'Compare APRs before borrowing.','original'),
('113.76.d.8.A',4,'Why does starting to invest early matter?','["early investors pay no taxes", "investments cannot lose value", "compound interest grows earnings on earlier earnings", "interest rates never change"]'::jsonb,2,'Time multiplies growth.','original'),
('113.76.d.8.B',4,'Using the Rule of 72, about how many years will it take money to double at 6% interest?','["10 years", "6 years", "72 years", "12 years"]'::jsonb,3,'72 divided by 6 equals 12.','original'),
('113.76.d.8.B',4,'Using the Rule of 72, about how many years will it take money to double at 8% interest?','["9 years", "12 years", "7 years", "8 years"]'::jsonb,0,'72 divided by 8 equals 9.','original'),
('113.76.d.8.C',3,'A certificate of deposit (CD) typically does what?','["is a type of stock", "pays a fixed interest rate if you keep money in for a set term", "has no interest", "lets you withdraw anytime without penalty"]'::jsonb,1,'Early withdrawal often costs a penalty.','original'),
('113.76.d.8.C',3,'A bank savings account is considered what?','["a stock", "uninsured", "low risk and easy to access, with low returns", "high risk with high returns"]'::jsonb,2,'FDIC insurance protects deposits.','original'),
('113.76.d.8.D',3,'Compared with bonds, stocks generally have what?','["no risk", "guaranteed return", "lower risk and lower return", "higher potential return and higher risk"]'::jsonb,3,'Risk and return are linked.','original'),
('113.76.d.8.D',3,'A mutual fund does what?','["pools money from many investors to buy a variety of investments", "is a loan", "guarantees profits", "is a savings account"]'::jsonb,0,'Diversification reduces risk.','original'),
('113.76.d.8.D',3,'Diversification means what?','["avoiding all investments", "spreading investments across different assets", "only buying bonds", "putting everything in one stock"]'::jsonb,1,'It reduces the effect of any one loss.','original'),
('113.76.d.8.E',3,'A traditional 401(k) or IRA contribution is typically what?','["a loan", "never taxed", "pre-tax, reducing taxable income now", "post-tax with tax-free growth"]'::jsonb,2,'Withdrawals are taxed in retirement.','original'),
('113.76.d.8.E',3,'A Roth IRA is funded with what?','["pre-tax money only", "employer money only", "borrowed money", "after-tax money, with qualified withdrawals tax-free"]'::jsonb,3,'Taxes are paid up front.','original'),
('113.76.d.8.F',3,'An emergency fund is meant to cover what?','["unexpected expenses", "daily snacks", "luxury items", "planned vacations"]'::jsonb,0,'Experts often suggest three to six months of expenses.','original'),
('113.76.d.8.G',3,'Saving for a down payment on a home is what kind of goal?','["a retirement goal", "an intermediate-term goal", "a short-term goal", "an impossible goal"]'::jsonb,1,'Goals that take several years are intermediate.','original'),
('113.76.d.8.H',3,'Retirement saving is what kind of goal?','["a short-term goal", "a one-week goal", "a long-term goal", "an immediate goal"]'::jsonb,2,'Time lets investments grow.','original'),
('113.76.d.8.H',3,'Investing small amounts regularly over decades helps because of what?','["no risk", "guaranteed gains", "lower taxes always", "compound growth"]'::jsonb,3,'Consistency builds wealth.','original'),
('113.76.d.9.A',3,'Buying insurance is an example of which risk strategy?','["transferring risk", "ignoring risk", "retaining all risk", "avoiding risk"]'::jsonb,0,'Insurers take on financial risk for a fee.','original'),
('113.76.d.9.A',3,'Not driving in dangerous weather is an example of which risk strategy?','["retaining risk", "avoiding risk", "transferring risk", "reducing risk"]'::jsonb,1,'You eliminate the exposure.','original'),
('113.76.d.9.B',3,'An insurance premium is what?','["a fee for filing a claim", "the amount paid before coverage begins", "the regular payment for coverage", "the claim payment"]'::jsonb,2,'Premiums are paid monthly or yearly.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
insert into public.question_bank (teks_code, teks_item_id, subject, grade_num, course, difficulty, qtype, prompt, choices, answer_idx, explanation, source, status, gen_batch)
select distinct on (v.prompt) v.code, i.id, d.subject,
       case when i.grade_level = 'K' then 0 when i.grade_level ~ '^[0-9]+' then substring(i.grade_level from '^[0-9]+')::smallint end,
       case when i.grade_level is null then i.grade_course_title end,
       v.diff, 'mc', v.prompt, v.choices, v.ans, v.expl, v.src, 'checked', 'hs_pfle_v1'
from (values
('113.76.d.9.B',3,'A deductible is what?','["the maximum payout", "a refund", "the monthly bill", "the amount you pay before insurance pays"]'::jsonb,3,'Higher deductibles often lower premiums.','original'),
('113.76.d.9.B',3,'A co-pay is what?','["a fixed fee paid for a covered service", "a loan", "a policy limit", "a tax"]'::jsonb,0,'You might pay $25 per doctor visit.','original'),
('113.76.d.9.C',3,'Health insurance protects against what?','["weather damage", "high medical costs", "car repairs", "job loss"]'::jsonb,1,'It shares the cost of care.','original'),
('113.76.d.9.D',3,'Disability insurance replaces what?','["your home", "your investments", "part of your income if you cannot work", "your car"]'::jsonb,2,'It protects earning power.','original'),
('113.76.d.9.D',3,'Long-term care insurance helps pay for what?','["a vacation", "college tuition", "a new car", "extended care such as nursing homes"]'::jsonb,3,'It covers costs not usually covered by health insurance.','original'),
('113.76.d.9.E',3,'Term life insurance provides coverage for what?','["a specific period of time", "only accidents", "your whole life with cash value", "any period you choose after buying"]'::jsonb,0,'It is generally cheaper than whole life.','original'),
('113.76.d.9.E',3,'Whole life insurance differs from term because it does what?','["costs nothing", "builds cash value and lasts a lifetime", "expires quickly", "has no premiums"]'::jsonb,1,'It usually costs more.','original'),
('113.76.d.9.F',3,'Homeowner''s insurance generally protects against what?','["medical bills", "stock losses", "damage to the home and belongings", "job loss"]'::jsonb,2,'It also covers liability.','original'),
('113.76.d.9.F',3,'Renter''s insurance protects what?','["the building structure", "the landlord''s income", "the mortgage", "the renter''s belongings"]'::jsonb,3,'The landlord''s policy covers the building.','original'),
('113.76.d.9.G',3,'A factor that can raise a driver''s auto insurance premium is what?','["accidents or traffic tickets", "being older than 40 with no claims", "defensive driving courses", "a clean record"]'::jsonb,0,'Risk affects price.','original'),
('113.76.d.9.G',3,'Liability coverage in auto insurance pays for what?','["your own car''s repairs", "damage you cause to others", "your tires", "your gas"]'::jsonb,1,'Most states require it.','original'),
('113.76.d.9.H',3,'A good way to reduce the risk of identity theft is to do what?','["share your Social Security number freely", "use the same password everywhere", "protect personal information and use strong passwords", "ignore bank statements"]'::jsonb,2,'Guard your data.','original'),
('113.76.d.9.I',3,'A Ponzi scheme pays earlier investors using what?','["real profits from a business", "government funds", "bank interest", "money from newer investors"]'::jsonb,3,'It collapses when new money stops.','original'),
('113.76.d.9.I',3,'A common sign of a financial scam is what?','["promises of guaranteed high returns with no risk", "regulated advisers", "clear written terms", "slow steady returns"]'::jsonb,0,'If it sounds too good to be true, it probably is.','original'),
('113.76.d.9.J',3,'The Consumer Financial Protection Bureau (CFPB) does what?','["prints currency", "protects consumers in financial products and services", "collects income tax", "sets stock prices"]'::jsonb,1,'It takes complaints and enforces rules.','original'),
('113.76.d.9.K',3,'An estate plan, including a will, does what?','["replaces insurance", "pays off debts automatically", "directs how property goes and names a guardian for minor children", "avoids all taxes"]'::jsonb,2,'Planning protects family.','original'),
('113.76.d.10.A',3,'After identifying a money problem, what is the next step in decision making?','["ignore alternatives", "end the process", "choose at random", "gather information and list options"]'::jsonb,3,'Information precedes choosing.','original'),
('113.76.d.10.B',3,'A good budget should include which parts?','["income, fixed and flexible expenses, and savings", "only income", "only wants", "only debts"]'::jsonb,0,'Plan for goals as well as bills.','original'),
('113.76.d.10.B',3,'A common budgeting guideline sets aside about 20% of income for what?','["entertainment only", "savings and debt repayment", "gifts only", "clothes only"]'::jsonb,1,'The 50/30/20 rule splits needs, wants and savings.','original'),
('113.76.d.10.C',3,'Why do earning, spending, credit, saving and risk management matter?','["they never change", "only wealthy people use them", "they affect one another and a person''s financial well-being", "they are unrelated"]'::jsonb,2,'Good choices in each area support stability.','original')
) as v(code, diff, prompt, choices, ans, expl, src)
join public.teks_items i on i.code = v.code and i.is_standard
join public.teks_documents d on d.id = i.document_id and d.subject = 'Social Studies' and d.language = 'en'
on conflict (fingerprint) do nothing;
