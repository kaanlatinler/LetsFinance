create table HisseData(
	HisseDataID int primary key identity,
	HisseID uniqueidentifier not null,
	HisseName nvarchar(100),
	HisseRate nvarchar(10),
	HisseTime nvarchar(10),
	HissePrice nvarchar(100)
)