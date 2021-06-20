-->WINDOW FUNCTIONS<--
--getting additional aggregation, next to group by, with window functions


--look for temp table in tempdb and drop if exists
IF OBJECT_ID(N'tempdb..#sales') IS NOT NULL
BEGIN
DROP TABLE #sales
END
GO

CREATE TABLE #sales
(
    SK         varchar(5), --surrogate key
    AgentID  varchar(10),
    ProductID   varchar(10),
    Price       decimal(10,0)
);
INSERT INTO #Sales
VALUES ('1', 'Agent1', 'Product1', 100),
       ('2', 'Agent1', 'Product1', 3000),
       ('3', 'Agent1', 'Product2', 1000),
	   ('4', 'Agent1', 'Product3', 500),
       ('5', 'Agent2', 'Product2', 2000),
       ('6', 'Agent2', 'Product3', 4000);


SELECT AgentID,
       ProductID,
       SUM(price) AS  Sales_Customer_Product,
       SUM(SUM(price)) OVER (PARTITION BY AgentID) AS Sales_Customer
FROM #sales
GROUP BY AgentID, productID
ORDER BY AgentID, productID