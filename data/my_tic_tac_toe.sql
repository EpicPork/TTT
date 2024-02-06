--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Homebrew)
-- Dumped by pg_dump version 15.4

-- Started on 2023-10-28 11:15:26 PDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16401)
-- Name: games; Type: TABLE; Schema: public; Owner: csair
--

CREATE TABLE public.games (
    game_id integer NOT NULL,
    user_id integer,
    board_size integer NOT NULL,
    outcome character varying(10)
);


ALTER TABLE public.games OWNER TO csair;

--
-- TOC entry 214 (class 1259 OID 16400)
-- Name: games_game_id_seq; Type: SEQUENCE; Schema: public; Owner: csair
--

CREATE SEQUENCE public.games_game_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.games_game_id_seq OWNER TO csair;

--
-- TOC entry 3665 (class 0 OID 0)
-- Dependencies: 214
-- Name: games_game_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: csair
--

ALTER SEQUENCE public.games_game_id_seq OWNED BY public.games.game_id;


--
-- TOC entry 218 (class 1259 OID 16424)
-- Name: leaderboard; Type: TABLE; Schema: public; Owner: csair
--

CREATE TABLE public.leaderboard (
    user_id integer,
    wins integer,
    losses integer
);


ALTER TABLE public.leaderboard OWNER TO csair;

--
-- TOC entry 217 (class 1259 OID 16413)
-- Name: moves; Type: TABLE; Schema: public; Owner: csair
--

CREATE TABLE public.moves (
    move_id integer NOT NULL,
    game_id integer,
    player character varying(10),
    position_x integer,
    position_y integer
);


ALTER TABLE public.moves OWNER TO csair;

--
-- TOC entry 216 (class 1259 OID 16412)
-- Name: moves_move_id_seq; Type: SEQUENCE; Schema: public; Owner: csair
--

CREATE SEQUENCE public.moves_move_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moves_move_id_seq OWNER TO csair;

--
-- TOC entry 3666 (class 0 OID 0)
-- Dependencies: 216
-- Name: moves_move_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: csair
--

ALTER SEQUENCE public.moves_move_id_seq OWNED BY public.moves.move_id;


--
-- TOC entry 224 (class 1259 OID 16467)
-- Name: player; Type: TABLE; Schema: public; Owner: csair
--

CREATE TABLE public.player (
    player_id integer NOT NULL,
    user_id integer,
    player_name character varying(255) NOT NULL,
    player_symbol character(1) NOT NULL
);


ALTER TABLE public.player OWNER TO csair;

--
-- TOC entry 223 (class 1259 OID 16466)
-- Name: player_player_id_seq; Type: SEQUENCE; Schema: public; Owner: csair
--

CREATE SEQUENCE public.player_player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.player_player_id_seq OWNER TO csair;

--
-- TOC entry 3667 (class 0 OID 0)
-- Dependencies: 223
-- Name: player_player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: csair
--

ALTER SEQUENCE public.player_player_id_seq OWNED BY public.player.player_id;


--
-- TOC entry 219 (class 1259 OID 16432)
-- Name: playerstats; Type: TABLE; Schema: public; Owner: csair
--

CREATE TABLE public.playerstats (
    user_id integer,
    total_wins integer,
    total_losses integer
);


ALTER TABLE public.playerstats OWNER TO csair;

--
-- TOC entry 220 (class 1259 OID 16440)
-- Name: trainingdata; Type: TABLE; Schema: public; Owner: csair
--

CREATE TABLE public.trainingdata (
    game_id integer,
    player character varying(10),
    position_x integer,
    position_y integer
);


ALTER TABLE public.trainingdata OWNER TO csair;

--
-- TOC entry 222 (class 1259 OID 16456)
-- Name: useraccount; Type: TABLE; Schema: public; Owner: csair
--

CREATE TABLE public.useraccount (
    user_id integer NOT NULL,
    username character varying(50) NOT NULL,
    password character varying(255) NOT NULL,
    email character varying(100) NOT NULL
);


ALTER TABLE public.useraccount OWNER TO csair;

--
-- TOC entry 221 (class 1259 OID 16455)
-- Name: useraccount_user_id_seq; Type: SEQUENCE; Schema: public; Owner: csair
--

CREATE SEQUENCE public.useraccount_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.useraccount_user_id_seq OWNER TO csair;

--
-- TOC entry 3668 (class 0 OID 0)
-- Dependencies: 221
-- Name: useraccount_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: csair
--

ALTER SEQUENCE public.useraccount_user_id_seq OWNED BY public.useraccount.user_id;


--
-- TOC entry 3488 (class 2604 OID 16404)
-- Name: games game_id; Type: DEFAULT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.games ALTER COLUMN game_id SET DEFAULT nextval('public.games_game_id_seq'::regclass);


--
-- TOC entry 3489 (class 2604 OID 16416)
-- Name: moves move_id; Type: DEFAULT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.moves ALTER COLUMN move_id SET DEFAULT nextval('public.moves_move_id_seq'::regclass);


--
-- TOC entry 3491 (class 2604 OID 16470)
-- Name: player player_id; Type: DEFAULT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.player ALTER COLUMN player_id SET DEFAULT nextval('public.player_player_id_seq'::regclass);


--
-- TOC entry 3490 (class 2604 OID 16459)
-- Name: useraccount user_id; Type: DEFAULT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.useraccount ALTER COLUMN user_id SET DEFAULT nextval('public.useraccount_user_id_seq'::regclass);


--
-- TOC entry 3650 (class 0 OID 16401)
-- Dependencies: 215
-- Data for Name: games; Type: TABLE DATA; Schema: public; Owner: csair
--

COPY public.games (game_id, user_id, board_size, outcome) FROM stdin;
\.


--
-- TOC entry 3653 (class 0 OID 16424)
-- Dependencies: 218
-- Data for Name: leaderboard; Type: TABLE DATA; Schema: public; Owner: csair
--

COPY public.leaderboard (user_id, wins, losses) FROM stdin;
\.


--
-- TOC entry 3652 (class 0 OID 16413)
-- Dependencies: 217
-- Data for Name: moves; Type: TABLE DATA; Schema: public; Owner: csair
--

COPY public.moves (move_id, game_id, player, position_x, position_y) FROM stdin;
\.


--
-- TOC entry 3659 (class 0 OID 16467)
-- Dependencies: 224
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: csair
--

COPY public.player (player_id, user_id, player_name, player_symbol) FROM stdin;
\.


--
-- TOC entry 3654 (class 0 OID 16432)
-- Dependencies: 219
-- Data for Name: playerstats; Type: TABLE DATA; Schema: public; Owner: csair
--

COPY public.playerstats (user_id, total_wins, total_losses) FROM stdin;
\.


--
-- TOC entry 3655 (class 0 OID 16440)
-- Dependencies: 220
-- Data for Name: trainingdata; Type: TABLE DATA; Schema: public; Owner: csair
--

COPY public.trainingdata (game_id, player, position_x, position_y) FROM stdin;
\.


--
-- TOC entry 3657 (class 0 OID 16456)
-- Dependencies: 222
-- Data for Name: useraccount; Type: TABLE DATA; Schema: public; Owner: csair
--

COPY public.useraccount (user_id, username, password, email) FROM stdin;
\.


--
-- TOC entry 3669 (class 0 OID 0)
-- Dependencies: 214
-- Name: games_game_id_seq; Type: SEQUENCE SET; Schema: public; Owner: csair
--

SELECT pg_catalog.setval('public.games_game_id_seq', 1, false);


--
-- TOC entry 3670 (class 0 OID 0)
-- Dependencies: 216
-- Name: moves_move_id_seq; Type: SEQUENCE SET; Schema: public; Owner: csair
--

SELECT pg_catalog.setval('public.moves_move_id_seq', 1, false);


--
-- TOC entry 3671 (class 0 OID 0)
-- Dependencies: 223
-- Name: player_player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: csair
--

SELECT pg_catalog.setval('public.player_player_id_seq', 1, false);


--
-- TOC entry 3672 (class 0 OID 0)
-- Dependencies: 221
-- Name: useraccount_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: csair
--

SELECT pg_catalog.setval('public.useraccount_user_id_seq', 1, false);


--
-- TOC entry 3493 (class 2606 OID 16406)
-- Name: games games_pkey; Type: CONSTRAINT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (game_id);


--
-- TOC entry 3495 (class 2606 OID 16418)
-- Name: moves moves_pkey; Type: CONSTRAINT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.moves
    ADD CONSTRAINT moves_pkey PRIMARY KEY (move_id);


--
-- TOC entry 3503 (class 2606 OID 16472)
-- Name: player player_pkey; Type: CONSTRAINT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_pkey PRIMARY KEY (player_id);


--
-- TOC entry 3497 (class 2606 OID 16465)
-- Name: useraccount useraccount_email_key; Type: CONSTRAINT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.useraccount
    ADD CONSTRAINT useraccount_email_key UNIQUE (email);


--
-- TOC entry 3499 (class 2606 OID 16461)
-- Name: useraccount useraccount_pkey; Type: CONSTRAINT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.useraccount
    ADD CONSTRAINT useraccount_pkey PRIMARY KEY (user_id);


--
-- TOC entry 3501 (class 2606 OID 16463)
-- Name: useraccount useraccount_username_key; Type: CONSTRAINT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.useraccount
    ADD CONSTRAINT useraccount_username_key UNIQUE (username);


--
-- TOC entry 3504 (class 2606 OID 16419)
-- Name: moves moves_game_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.moves
    ADD CONSTRAINT moves_game_id_fkey FOREIGN KEY (game_id) REFERENCES public.games(game_id);


--
-- TOC entry 3506 (class 2606 OID 16473)
-- Name: player player_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.useraccount(user_id);


--
-- TOC entry 3505 (class 2606 OID 16443)
-- Name: trainingdata trainingdata_game_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: csair
--

ALTER TABLE ONLY public.trainingdata
    ADD CONSTRAINT trainingdata_game_id_fkey FOREIGN KEY (game_id) REFERENCES public.games(game_id);


-- Completed on 2023-10-28 11:15:26 PDT

--
-- PostgreSQL database dump complete
--

