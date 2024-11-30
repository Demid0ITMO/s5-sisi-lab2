%%%%%%%%%%%%%%%%%%%%%% ФАКТЫ С 1 АРГУМЕНТОМ %%%%%%%%%%%%%%%%%%%%%%%

% Факты: Игры
game(minecraft).
game(fortnite).
game(pubg).
game(overwatch).
game(dnd).
game(skyrim).
game(gta5).
game(zelda).
game(rocket_league).
game(among_us).

% Факты: Жанры игр
genre(action).
genre(strategy).
genre(adventure).
genre(role_playing).
genre(sports).

% Факты: Платформы игр (где можно играть)
platform(pc).
platform(playstation).
platform(xbox).
platform(nintendo_switch).

% Факты: Режим игры
mode(single_player).
mode(multi_player).
mode(cooperative).
mode(competitive).

% Факты: Возрастной рейтинг
rating(e).
rating(e10).
rating(t).
rating(m).
rating(ao).

%%%%%%%%%%%%%%%%%%%%%% ФАКТЫ С 2 АРГУМЕНТАМИ %%%%%%%%%%%%%%%%%%%%%%

% Факты: Игра X имеет жанр Y
has_genre(minecraft, adventure).
has_genre(minecraft, strategy).
has_genre(fortnite, action).
has_genre(fortnite, strategy).
has_genre(pubg, action).
has_genre(overwatch, action).
has_genre(dnd, role_playing).
has_genre(skyrim, role_playing).
has_genre(gta5, action).
has_genre(zelda, adventure).
has_genre(rocket_league, sports).
has_genre(among_us, strategy).

% Факты: В игру X можно играть на Y
has_platform(minecraft, pc).
has_platform(minecraft, playstation).
has_platform(minecraft, xbox).
has_platform(minecraft, nintendo_switch).
has_platform(fortnite, pc).
has_platform(fortnite, playstation).
has_platform(fortnite, xbox).
has_platform(fortnite, nintendo_switch).
has_platform(pubg, pc).
has_platform(pubg, xbox).
has_platform(overwatch, pc).
has_platform(overwatch, playstation).
has_platform(overwatch, xbox).
has_platform(dnd, pc).
has_platform(skyrim, pc).
has_platform(skyrim, playstation).
has_platform(gta5, pc).
has_platform(gta5, playstation).
has_platform(gta5, xbox).
has_platform(zelda, nintendo_switch).
has_platform(rocket_league, pc).
has_platform(rocket_league, playstation).
has_platform(rocket_league, xbox).
has_platform(among_us, pc).
has_platform(among_us, nintendo_switch).

% Факты: Игра X имеет Y режим
has_mode(minecraft, single_player).
has_mode(fortnite, multi_player).
has_mode(pubg, competitive).

% Факты: Игра Х имеет возрастное ограничение Y
has_rating(minecraft, e).
has_rating(fortnite, t).
has_rating(pubg, t).
has_rating(overwatch, t).
has_rating(dnd, t).
has_rating(skyrim, m).
has_rating(gta5, m).
has_rating(zelda, e10).
has_rating(rocket_league, e).
has_rating(among_us, t).

% Факты: В игре X есть персонаж Y
has_character(minecraft, steve).
has_character(fortnite, default_skin).

%%%%%%%%%%%%%%%%%%%%%%%%%%%% ПРАВИЛА %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Является ли игра Game кооперативной ролевой игрой
cooperative_rpg_game(Game) :- has_mode(Game, cooperative), has_genre(Game, role_playing).

% Является ли игра Game взрослой (с рейтингом adults only) стратегией на xbox
adult_xbox_strategy_game(Game) :-
    has_genre(Game, strategy),
    has_platform(Game, xbox),
    has_rating(Game, ao).

% Является ли игра Game мультиплеерным экшеном на консоли
team_based_console_game(Game) :-
    has_genre(Game, action),
    (has_platform(Game, playstation); has_platform(Game, nintendo_switch)),
    has_mode(Game, multi_player).

% Является ли игра Game подходящей для детей
suitable_for_kids(Game) :-
    (has_rating(Game, e); has_rating(Game, e10)),
    has_genre(Game, adventure),
    (has_platform(Game, pc); has_platform(Game, nintendo_switch)),
    has_mode(Game, single_player).

% Является ли игра Game подростковой игрой на платформе Platform
teen_friendly_game(Game, Platform) :-
    has_platform(Game, Platform),
    (has_rating(Game, e); has_rating(Game, e10); has_rating(Game, t)).
