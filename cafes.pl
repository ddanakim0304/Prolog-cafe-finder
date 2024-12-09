distance(cafe1, 0.5).
price(cafe1, $).
wifi(cafe1, yes).
sockets(cafe1, yes).
vegan(cafe1, yes).
cash_discount(cafe1, no).
days_opened(cafe1, [monday, tuesday, wednesday, thursday, friday]).
open_hour(cafe1, 9).
close_hour(cafe1, 17).

% Rules
suitable_cafe(Cafe, MaxDistance, Price, Wifi, Sockets, Vegan, CashDiscountPref, VisitDay, VisitStart, VisitEnd) :-
    distance(Cafe, D), D =< MaxDistance,
    price(Cafe, Price),
    wifi(Cafe, Wifi),
    sockets(Cafe, Sockets),
    vegan(Cafe, Vegan),
    (CashDiscountPref = yes -> cash_discount(Cafe, yes) ; true),
    days_opened(Cafe, Days), member(VisitDay, Days),
    open_hour(Cafe, Open), close_hour(Cafe, Close),
    VisitStart >= Open, VisitEnd =< Close.
