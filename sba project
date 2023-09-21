program project1;

uses SysUtils, testing;
var
  paragraph : TStringArray;
  inputStr, word: string;
  length: integer;
  words: set;

function SearchInDictionary(arr: TIntArray; target, low, high: Integer): Boolean;
var
  mid: Integer;
begin
  while low <= high do
  begin
    mid := (low + high) div 2;

    if arr[mid] = target then
    begin
      BinarySearch := True;
      Exit;
    end
    else if arr[mid] < target then
      low := mid + 1
    else
      high := mid - 1;
  end;

  BinarySearch := False;
end;

//procedure ExcludeCommonWords(var words: TWordSet; const common_words: TWordSet);
var
  word: string;
begin
  for word in common_words do
    exclude(words, word);
end;
/////
procedure IncludeWords(var words: TWordSet; const paragraph: Tstringarray)
var
  word: string
begin
//put words into set
  for word in paragraph do
     include(words, i);
end;
//////
procedure ProcessWords(var words: TWordSet; const vocab: TStringArray);
var
  word: string;
  count: Integer;
begin
  count := 0;
  for word in words do
  begin
    SetLength(myArray, count + 1);
    vocab[count] := word;
    Inc(count);
  end;
end;

begin
  writeln('Input a passage: ');
  readln(inputStr);
  paragraph := inputStr.Split(' '):
  deletewords(SearchInDictionary);
  ProcessWords;

//search the word in dictionary



  InitializeArray(arr, numElements);

  low := 1;
  high := Length(arr);
  for k in words do
      begin
        found := BinarySearch(arr, target, low, high);
        if found then
           Delete the element in array
      end
  for i := Low(arr) to High(arr) do
  begin
    elementsInLine := elementsInLine + IntToStr(arr[i]) + ' ';
  end;

  procedure PrintWordsInArray(const words: TStringArray);
var
  i: Integer;
begin
  writeln('Words in the array:');
  for i := 0 to Length(words) - 1 do
  begin
    writeln(words[i]);
  end;
end;
  Readln;
end.


