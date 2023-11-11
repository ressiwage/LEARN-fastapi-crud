--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: main; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA main;


ALTER SCHEMA main OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: customers; Type: TABLE; Schema: main; Owner: postgres
--

CREATE TABLE main.customers (
    id bigint NOT NULL,
    name text,
    surname text,
    age integer
);


ALTER TABLE main.customers OWNER TO postgres;

--
-- Name: customers_id_seq; Type: SEQUENCE; Schema: main; Owner: postgres
--

CREATE SEQUENCE main.customers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE main.customers_id_seq OWNER TO postgres;

--
-- Name: customers_id_seq; Type: SEQUENCE OWNED BY; Schema: main; Owner: postgres
--

ALTER SEQUENCE main.customers_id_seq OWNED BY main.customers.id;


--
-- Name: products; Type: TABLE; Schema: main; Owner: postgres
--

CREATE TABLE main.products (
    id bigint NOT NULL,
    name text,
    price double precision,
    "idPhoto" integer NOT NULL
);


ALTER TABLE main.products OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: main; Owner: postgres
--

CREATE SEQUENCE main.products_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE main.products_id_seq OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: main; Owner: postgres
--

ALTER SEQUENCE main.products_id_seq OWNED BY main.products.id;


--
-- Name: transactions; Type: TABLE; Schema: main; Owner: postgres
--

CREATE TABLE main.transactions (
    id bigint NOT NULL,
    "idCustomer" bigint NOT NULL,
    "idProduct" bigint NOT NULL
);


ALTER TABLE main.transactions OWNER TO postgres;

--
-- Name: transactions_id_seq; Type: SEQUENCE; Schema: main; Owner: postgres
--

CREATE SEQUENCE main.transactions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE main.transactions_id_seq OWNER TO postgres;

--
-- Name: transactions_id_seq; Type: SEQUENCE OWNED BY; Schema: main; Owner: postgres
--

ALTER SEQUENCE main.transactions_id_seq OWNED BY main.transactions.id;


--
-- Name: customers id; Type: DEFAULT; Schema: main; Owner: postgres
--

ALTER TABLE ONLY main.customers ALTER COLUMN id SET DEFAULT nextval('main.customers_id_seq'::regclass);


--
-- Name: products id; Type: DEFAULT; Schema: main; Owner: postgres
--

ALTER TABLE ONLY main.products ALTER COLUMN id SET DEFAULT nextval('main.products_id_seq'::regclass);


--
-- Name: transactions id; Type: DEFAULT; Schema: main; Owner: postgres
--

ALTER TABLE ONLY main.transactions ALTER COLUMN id SET DEFAULT nextval('main.transactions_id_seq'::regclass);


--
-- Data for Name: customers; Type: TABLE DATA; Schema: main; Owner: postgres
--

COPY main.customers (id, name, surname, age) FROM stdin;
2	игнат	панов	54
1	михаил	ефимов	21
3	александр	петров	81
0	михаил	кузнецов	16
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: main; Owner: postgres
--

COPY main.products (id, name, price, "idPhoto") FROM stdin;
1	энергетик драйв	69.9	1
2	сигареты марльборо	200	2
\.


--
-- Data for Name: transactions; Type: TABLE DATA; Schema: main; Owner: postgres
--

COPY main.transactions (id, "idCustomer", "idProduct") FROM stdin;
1	1	2
2	1	2
3	2	1
\.


--
-- Name: customers_id_seq; Type: SEQUENCE SET; Schema: main; Owner: postgres
--

SELECT pg_catalog.setval('main.customers_id_seq', 1, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: main; Owner: postgres
--

SELECT pg_catalog.setval('main.products_id_seq', 2, true);


--
-- Name: transactions_id_seq; Type: SEQUENCE SET; Schema: main; Owner: postgres
--

SELECT pg_catalog.setval('main.transactions_id_seq', 3, true);


--
-- Name: customers customers_pkey; Type: CONSTRAINT; Schema: main; Owner: postgres
--

ALTER TABLE ONLY main.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (id);


--
-- Name: products pk_id; Type: CONSTRAINT; Schema: main; Owner: postgres
--

ALTER TABLE ONLY main.products
    ADD CONSTRAINT pk_id PRIMARY KEY (id);


--
-- Name: transactions transactions_pkey; Type: CONSTRAINT; Schema: main; Owner: postgres
--

ALTER TABLE ONLY main.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (id);


--
-- Name: transactions fk_c; Type: FK CONSTRAINT; Schema: main; Owner: postgres
--

ALTER TABLE ONLY main.transactions
    ADD CONSTRAINT fk_c FOREIGN KEY ("idCustomer") REFERENCES main.customers(id);


--
-- Name: transactions fk_p; Type: FK CONSTRAINT; Schema: main; Owner: postgres
--

ALTER TABLE ONLY main.transactions
    ADD CONSTRAINT fk_p FOREIGN KEY ("idProduct") REFERENCES main.products(id);


--
-- PostgreSQL database dump complete
--

