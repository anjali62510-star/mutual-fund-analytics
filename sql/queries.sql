-- =====================================================
-- 1. Top 5 Fund Houses by AUM
-- =====================================================

SELECT
    fund_house,
    MAX(aum_crore) AS max_aum_crore
FROM "03_aum_by_fund_house"
GROUP BY fund_house
ORDER BY max_aum_crore DESC
LIMIT 5;


-- =====================================================
-- 2. Average NAV by Fund
-- =====================================================

SELECT
    amfi_code,
    ROUND(AVG(nav), 2) AS avg_nav
FROM "02_nav_history"
GROUP BY amfi_code
ORDER BY avg_nav DESC;


-- =====================================================
-- 3. Monthly SIP Growth
-- =====================================================

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM "04_monthly_sip_inflows"
ORDER BY month;


-- =====================================================
-- 4. Transactions by State
-- =====================================================

SELECT
    state,
    COUNT(*) AS transaction_count
FROM "08_investor_transactions"
GROUP BY state
ORDER BY transaction_count DESC;


-- =====================================================
-- 5. Funds with Expense Ratio Below 1%
-- =====================================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM "07_scheme_performance"
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;


-- =====================================================
-- 6. Top 10 Funds by 5-Year Return
-- =====================================================

SELECT
    scheme_name,
    return_5yr_pct
FROM "07_scheme_performance"
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- =====================================================
-- 7. Top 10 Funds by Sharpe Ratio
-- =====================================================

SELECT
    scheme_name,
    sharpe_ratio
FROM "07_scheme_performance"
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- =====================================================
-- 8. Category-wise Net Inflows
-- =====================================================

SELECT
    category,
    ROUND(SUM(net_inflow_crore),2) AS total_inflow
FROM "05_category_inflows"
GROUP BY category
ORDER BY total_inflow DESC;


-- =====================================================
-- 9. Risk Grade Distribution
-- =====================================================

SELECT
    risk_grade,
    COUNT(*) AS scheme_count
FROM "07_scheme_performance"
GROUP BY risk_grade
ORDER BY scheme_count DESC;


-- =====================================================
-- 10. Portfolio Sector Allocation
-- =====================================================

SELECT
    sector,
    ROUND(SUM(weight_pct),2) AS total_weight_pct
FROM "09_portfolio_holdings"
GROUP BY sector
ORDER BY total_weight_pct DESC;