program MariaDB;

{$APPTYPE CONSOLE}

uses
  System.SysUtils,
  FireDAC.Stan.Def,
  FireDAC.Stan.Async,
  FireDAC.Phys.MySQL,
  FireDAC.Phys.MySQLDef,
  FireDAC.Comp.Client,
  FireDAC.DApt;

var
  FDConnection: TFDConnection;
  FDQuery: TFDQuery;
begin
  try
    FDConnection := TFDConnection.Create(nil);
    FDQuery := TFDQuery.Create(nil);
    try
      with TFDPhysMySQLConnectionDefParams(FDConnection.Params) do
      begin
        DriverID := 'MySQL';
        Server   := '<$hostname>';
        Port     := <$port>;
        Database := '<$database>';
        UserName := '<$user>';
        Password := '<$password>';
      end;
      FDConnection.LoginPrompt := False;
      FDConnection.Open;

      FDQuery.Connection := FDConnection;
      FDQuery.Open('SELECT 1+1 AS FIELD');

      Writeln(FDQuery.FieldByName('FIELD').AsString);
    finally
      FreeAndNil(FDQuery);
      FreeAndNil(FDConnection);
    end;
  except on E: Exception do
    Writeln(E.ClassName, ': ', E.Message);
  end;
  Readln;
end.