create table CardData(
	CardDataID int primary key identity,
	CardID uniqueidentifier not null,
	CardName nvarchar(100),
	CardSellPrice nvarchar(10),
	CardBuyPrice nvarchar(10),
	CardIco nvarchar(20)
)