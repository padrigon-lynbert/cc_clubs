--
-- PostgreSQL database dump
--

\restrict Je3xxBNqTlveHTZaF3rIJgbOLYMh98Bov5uqLXiXqhXAaehsPdVYhuLrD6tZMCP

-- Dumped from database version 17.6 (Debian 17.6-1.pgdg12+1)
-- Dumped by pg_dump version 17.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE ONLY public.memberships DROP CONSTRAINT memberships_student_id_313d85d2_fk_users_id;
ALTER TABLE ONLY public.memberships DROP CONSTRAINT memberships_club_id_afa12c8a_fk_clubs_clubs_id;
ALTER TABLE ONLY public.member_application DROP CONSTRAINT member_application_student_id_128aa47d_fk_users_id;
ALTER TABLE ONLY public.member_application DROP CONSTRAINT member_application_club_id_6eeb5a4c_fk_clubs_clubs_id;
ALTER TABLE ONLY public.event DROP CONSTRAINT events_club_id_95a77c27_fk_clubs_id;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
ALTER TABLE ONLY public.clubs DROP CONSTRAINT clubs_location_id_c6daedcf_fk_school_branch_id;
ALTER TABLE ONLY public.clubs DROP CONSTRAINT clubs_chairperson_id_45ead6d3_fk_users_id;
ALTER TABLE ONLY public.clubs DROP CONSTRAINT clubs_adviser_id_c523bbd9_fk_users_id;
ALTER TABLE ONLY public.club_application DROP CONSTRAINT club_application_submitted_by_id_e93f892e_fk_users_id;
ALTER TABLE ONLY public.club_application DROP CONSTRAINT club_application_location_id_e9f5fd4a_fk_school_branch_id;
ALTER TABLE ONLY public.club_application DROP CONSTRAINT club_application_adviser_id_6740a8dc_fk_users_id;
ALTER TABLE ONLY public.budget_request DROP CONSTRAINT budget_requests_club_id_0e827e6f_fk_clubs_id;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
ALTER TABLE ONLY public.achievement DROP CONSTRAINT achievement_club_id_5573f7a6_fk_clubs_id;
DROP INDEX public.users_acc_no_55175e63_like;
DROP INDEX public.memberships_student_id_313d85d2;
DROP INDEX public.memberships_club_id_afa12c8a;
DROP INDEX public.member_application_student_id_128aa47d;
DROP INDEX public.member_application_club_id_6eeb5a4c;
DROP INDEX public.events_club_id_95a77c27;
DROP INDEX public.django_session_session_key_c0390e0f_like;
DROP INDEX public.django_session_expire_date_a5c62663;
DROP INDEX public.django_admin_log_user_id_c564eba6;
DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
DROP INDEX public.clubs_location_id_c6daedcf;
DROP INDEX public.clubs_club_name_f15f2a92_like;
DROP INDEX public.clubs_chairperson_id_45ead6d3;
DROP INDEX public.clubs_adviser_id_c523bbd9;
DROP INDEX public.clubs_acronym_d3a8cb64_like;
DROP INDEX public.club_application_submitted_by_id_e93f892e;
DROP INDEX public.club_application_location_id_e9f5fd4a;
DROP INDEX public.club_application_club_name_ac9cae06_like;
DROP INDEX public.club_application_adviser_id_6740a8dc;
DROP INDEX public.club_application_acronym_11f8eeae_like;
DROP INDEX public.budget_requests_club_id_0e827e6f;
DROP INDEX public.auth_user_username_6821ab7c_like;
DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
DROP INDEX public.auth_user_groups_group_id_97559544;
DROP INDEX public.auth_permission_content_type_id_2f476e4b;
DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
DROP INDEX public.auth_group_name_a6ea08ec_like;
DROP INDEX public.achievement_club_id_5573f7a6;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_acc_no_key;
ALTER TABLE ONLY public.memberships DROP CONSTRAINT unique_membership;
ALTER TABLE ONLY public.school_branch DROP CONSTRAINT school_branch_pkey;
ALTER TABLE ONLY public.memberships DROP CONSTRAINT memberships_pkey;
ALTER TABLE ONLY public.member_application DROP CONSTRAINT member_application_pkey;
ALTER TABLE ONLY public.event DROP CONSTRAINT events_pkey;
ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
ALTER TABLE ONLY public.clubs DROP CONSTRAINT clubs_clubs_pkey;
ALTER TABLE ONLY public.clubs DROP CONSTRAINT clubs_club_name_f15f2a92_uniq;
ALTER TABLE ONLY public.clubs DROP CONSTRAINT clubs_acronym_key;
ALTER TABLE ONLY public.club_application DROP CONSTRAINT club_application_pkey;
ALTER TABLE ONLY public.club_application DROP CONSTRAINT club_application_club_name_key;
ALTER TABLE ONLY public.club_application DROP CONSTRAINT club_application_acronym_key;
ALTER TABLE ONLY public.budget_request DROP CONSTRAINT budget_requests_pkey;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
ALTER TABLE ONLY public.achievement DROP CONSTRAINT achievement_pkey;
DROP TABLE public.users;
DROP TABLE public.school_branch;
DROP TABLE public.memberships;
DROP TABLE public.member_application;
DROP TABLE public.event;
DROP TABLE public.django_session;
DROP TABLE public.django_migrations;
DROP TABLE public.django_content_type;
DROP TABLE public.django_admin_log;
DROP TABLE public.clubs;
DROP TABLE public.club_application;
DROP TABLE public.budget_request;
DROP TABLE public.auth_user_user_permissions;
DROP TABLE public.auth_user_groups;
DROP TABLE public.auth_user;
DROP TABLE public.auth_permission;
DROP TABLE public.auth_group_permissions;
DROP TABLE public.auth_group;
DROP TABLE public.achievement;
-- *not* dropping schema, since initdb creates it
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

-- *not* creating schema, since initdb creates it


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: achievement; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.achievement (
    id bigint NOT NULL,
    title character varying(50) NOT NULL,
    details text,
    date_posted timestamp with time zone NOT NULL,
    club_id bigint NOT NULL
);


--
-- Name: achievement_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.achievement ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.achievement_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: budget_request; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.budget_request (
    id bigint NOT NULL,
    purpose character varying(255) NOT NULL,
    details text,
    amount numeric(10,2) NOT NULL,
    status integer NOT NULL,
    club_id bigint NOT NULL
);


--
-- Name: budget_requests_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.budget_request ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.budget_requests_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: club_application; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.club_application (
    id bigint NOT NULL,
    club_name character varying(255) NOT NULL,
    date_submitted timestamp with time zone NOT NULL,
    description text,
    status integer NOT NULL,
    submitted_by_id bigint,
    location_id bigint NOT NULL,
    banner character varying(100),
    acronym character varying(30),
    adviser_id bigint,
    email character varying(255),
    year_level character varying(10)
);


--
-- Name: club_application_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.club_application ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.club_application_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: clubs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.clubs (
    id bigint NOT NULL,
    club_name character varying(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    location_id bigint NOT NULL,
    description text,
    acronym character varying(30),
    adviser_id bigint,
    banner character varying(100),
    chairperson_id bigint,
    email character varying(255),
    is_active boolean NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    year_level character varying(10)
);


--
-- Name: clubs_clubs_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.clubs ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.clubs_clubs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- Name: event; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.event (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    description character varying(255),
    start_date timestamp with time zone NOT NULL,
    end_date timestamp with time zone NOT NULL,
    club_id bigint NOT NULL
);


--
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.event ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.events_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: member_application; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.member_application (
    id bigint NOT NULL,
    medical_form character varying(100) NOT NULL,
    certificate_of_recognition character varying(100) NOT NULL,
    student_id_card character varying(100) NOT NULL,
    date_submitted date NOT NULL,
    club_id bigint NOT NULL,
    student_id bigint NOT NULL
);


--
-- Name: member_application_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.member_application ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.member_application_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: memberships; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.memberships (
    id bigint NOT NULL,
    date_joined date NOT NULL,
    is_officer boolean NOT NULL,
    club_id bigint NOT NULL,
    student_id bigint NOT NULL
);


--
-- Name: memberships_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.memberships ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.memberships_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: school_branch; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.school_branch (
    id bigint NOT NULL,
    branch_name character varying(30) NOT NULL
);


--
-- Name: school_branch_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.school_branch ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.school_branch_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    acc_no character varying(20) NOT NULL,
    password character varying(128) NOT NULL,
    name character varying(100) NOT NULL,
    role integer NOT NULL
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: achievement; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.achievement (id, title, details, date_posted, club_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add users	7	add_users
26	Can change users	7	change_users
27	Can delete users	7	delete_users
28	Can view users	7	view_users
29	Can add clubs	8	add_clubs
30	Can change clubs	8	change_clubs
31	Can delete clubs	8	delete_clubs
32	Can view clubs	8	view_clubs
33	Can add club application	9	add_clubapplication
34	Can change club application	9	change_clubapplication
35	Can delete club application	9	delete_clubapplication
36	Can view club application	9	view_clubapplication
37	Can add member application	10	add_memberapplication
38	Can change member application	10	change_memberapplication
39	Can delete member application	10	delete_memberapplication
40	Can view member application	10	view_memberapplication
41	Can add memberships	11	add_memberships
42	Can change memberships	11	change_memberships
43	Can delete memberships	11	delete_memberships
44	Can view memberships	11	view_memberships
45	Can add branch	12	add_branch
46	Can change branch	12	change_branch
47	Can delete branch	12	delete_branch
48	Can view branch	12	view_branch
49	Can add budget request	13	add_budgetrequest
50	Can change budget request	13	change_budgetrequest
51	Can delete budget request	13	delete_budgetrequest
52	Can view budget request	13	view_budgetrequest
53	Can add event	14	add_event
54	Can change event	14	change_event
55	Can delete event	14	delete_event
56	Can view event	14	view_event
57	Can add achievement	15	add_achievement
58	Can change achievement	15	change_achievement
59	Can delete achievement	15	delete_achievement
60	Can view achievement	15	view_achievement
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: budget_request; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.budget_request (id, purpose, details, amount, status, club_id) FROM stdin;
\.


--
-- Data for Name: club_application; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.club_application (id, club_name, date_submitted, description, status, submitted_by_id, location_id, banner, acronym, adviser_id, email, year_level) FROM stdin;
1	test	2025-08-27 11:43:07.667332+00	test description	0	2	1	club_applications/banners/hiep-duong-unsplash.jpg	\N	\N	\N	\N
\.


--
-- Data for Name: clubs; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.clubs (id, club_name, created_at, location_id, description, acronym, adviser_id, banner, chairperson_id, email, is_active, updated_at, year_level) FROM stdin;
14	Psychology Society	2025-08-29 03:57:04.939161+00	1	The Psychology Society is a student organization that promotes mental health awareness, academic growth, and meaningful student involvement.	PSYCH-SOC	2		1	bcppsychsociety@gmail.com	t	2025-08-29 03:57:04.939161+00	3rd Year
17	BCP TALENT CENTER	2025-08-29 03:57:05.557844+00	1	The BCP Talent Center is a student organization that develops artistic skills, supports creativity, and showcases talents in school events.	TLC	2		1	bcptalentcenter@gmail.com	t	2025-08-29 03:57:05.557844+00	3rd Year
18	Accounting Information System Society	2025-08-29 03:57:05.743249+00	1	The Accounting Information System Society (AISS) is a student organization that promotes academic excellence, leadership, and professionalism among BSAIS students.	AISS	2		1	aiss.orgg@gmail.com	t	2025-08-29 03:57:05.743249+00	3rd Year
5	Liga ng mga Aktibong Kabataan Sa Araling Panlipunan 	2025-08-24 01:23:21.949908+00	1	The Liga ng mga  Aktibong Kabataan Sa Araling Panlipunan (LAKAS) is a student group that promotes civic awareness, history, and youth leadership.	LAKAS	2	club_applications/banners/LAKAS.jpg	1	lakasbcp@gmail.com	t	2025-08-31 13:18:39.62716+00	3rd Year
6	Guild of English Majors	2025-08-28 06:19:51.800164+00	1	The Guild of English Majors (GEMs) is a student organization that supports English majors' growth through learning, leadership, and unity.	GEMs	2	club_applications/banners/GEMs.png	1	gemsbcpians@gmail.com	t	2025-08-31 13:18:40.216639+00	4th Year
7	Association of Computer Engineering Students	2025-08-28 06:19:52.015604+00	1	The Association of Computer Engineering Students (ACES) is a student group that supports computer engineering students' learning, leadership, and career growth.	ACES	2	club_applications/banners/ACES.png	1	xyvertucio@gmail.com	t	2025-08-31 13:18:40.59064+00	4th Year
8	Association of Cultural Art Club	2025-08-28 06:19:52.256648+00	1	The Cultural Art Club is a student organization that promotes creativity, leadership, and growth through cultural and academic activities.	ACAC	2	club_applications/banners/ACAC.png	1	johnpaulmullet88@gmail.com	t	2025-08-31 13:18:40.95037+00	3rd Year
10	Lucid Intelligence of Bright and Righteous Officers	2025-08-28 06:19:52.783049+00	1	The Lucid Intelligence of Bright and Righteous Officers (LIBRO) is a student organization that promotes unity, inclusiveness, and student empowerment through leadership and service.	LIBRO	2	club_applications/banners/LIBRO.jpg	1	bcp.ctelibro@mail.com	t	2025-08-31 13:18:41.670201+00	3rd Year
11	Wikang Filipino Instrumento sa Kaunlarang Akademya	2025-08-28 06:19:53.012862+00	1	The Wikang Filipino Instrumento sa Kaunlarang Akademya (WIKA) is a student organization that promotes and enriches the Filipino language through creative and educational activities.	WIKA	2	club_applications/banners/WIKA.png	1	kawika.filorg2021@gmail.com	t	2025-08-31 13:18:42.037921+00	4th Year
12	Entrepre Youth Organization 	2025-08-28 06:19:53.234384+00	1	The Entrepre Youth Organization (EYO) is a student group that develops entrepreneurship skills and prepares students for business careers.	EYO	2	club_applications/banners/EYO.jpeg	1	organizationentrepreyouth@gmail.com	t	2025-08-31 13:18:42.43635+00	4th Year
13	Group of Athletes and Leaders Association for Wellness	2025-08-28 06:19:53.460733+00	1	The Group of Athletes and Leaders Association for Wellness (GALAW) is a student group promoting health, growth, and active engagement.	GALAW	2	club_applications/banners/GALAW.jpeg	1	galawbpedorg@gmail.com	t	2025-08-31 13:18:42.809318+00	3rd Year
15	Technology, Exploratory, Creativeness and Hospitality Skills 	2025-08-29 03:57:05.139935+00	1	A BTLED academic organization that develops technical, creative, and livelihood skills, promoting leadership, innovation, and holistic growth through school and community activities.	TECHS	2	club_applications/banners/TECHS.jpg	1	princesstrinidad891@gmail.com	t	2025-08-31 13:18:43.181327+00	4th Year
16	Students' Interactive Guild for Mathematics Major	2025-08-29 03:57:05.340779+00	1	The Students’ Interactive Guild for Mathematics Majors (SIGMA) is a student organization that supports math majors through learning, creativity, and collaboration.	SIGMA	2	club_applications/banners/SIGMA.jpg	1	sigmabcpians23@gmail.com	t	2025-08-31 13:18:43.542634+00	4th Year
19	Human Resource Society 	2025-08-29 03:57:05.94409+00	1	The Human Resource Society (HRS) is a student organization that develops leadership, knowledge, and skills in human resource management.	HRS	2	club_applications/banners/HRS.jpg	1	bcphumanresourcesociety@gmail.com	t	2025-08-31 13:18:43.907406+00	4th Year
20	Regnum Scientiae Discipulus 	2025-08-29 03:57:06.145294+00	1	The official organization of Science Major students promoting unity, scientific inquiry, leadership, and academic growth through innovative programs and activities.	RSD	2	club_applications/banners/RSD.png	1	regnumscientaediscipulus@gmail.com	t	2025-08-31 13:18:44.26969+00	3rd Year
21	Leadership Association Program Including Services	2025-08-29 03:57:06.393909+00	1	An organization dedicated to leadership development, student engagement, and service-oriented projects that promote growth and success.	LAPIS	2	club_applications/banners/LAPIS.jpeg	1	sheyeirambuen@gmail.com	t	2025-08-31 13:18:44.631974+00	4th Year
22	Bestlink Library and Information Science Society	2025-08-29 03:57:06.595091+00	1	An academic organization for BLIS students promoting leadership, unity, library advocacy, and professional growth through collaborative programs and activities.	BLISS	2	club_applications/banners/BLISS.jpg	1	bcp.blisso@gmail.com	t	2025-08-31 13:18:44.995754+00	2nd Year
23	Tourism Student Society 	2025-08-29 03:57:06.796287+00	1	An academic organization for tourism students fostering leadership, creativity, civic engagement, and professional development through events and activities.	TSS	2	club_applications/banners/TSS.jpeg	1	mylenegammaru1994@gmail.com	t	2025-08-31 13:18:45.359746+00	4th Year
25	Guild Officers to Lead Development 	2025-08-29 03:57:07.198992+00	1	An organization supporting BSOA students by fostering leadership, professional growth, community engagement, and active student development.	GOLD	2	club_applications/banners/GOLD.jpg	1	kristine.lacaba.143@gmail.com	t	2025-08-31 13:18:46.108717+00	3rd Year
26	Shuttle Master Club 	2025-08-29 03:57:07.384979+00	1	A sports organization promoting badminton excellence, teamwork, discipline, and holistic development among student-athletes.	SMC	2	club_applications/banners/SMC.png	1	alibarrarealingo091102@gmail.com	t	2025-08-31 13:18:46.520368+00	4th Year
4	Computer Engineering Sports Club	2025-08-24 01:23:21.748661+00	1	The Computer Engineering Sports Club (CESC) is a student group that promotes health, growth, and active student engagement.	CESC	2	club_applications/banners/CESC_QsXWpOE.png	1	about.andrei.tolomia@gmail.com	t	2025-08-31 13:18:39.249248+00	3rd Year
9	Association of Computer Engineering Academic Driven Students	2025-08-28 06:19:52.534298+00	1	The Association of Computer Engineering Academic Driven Students (ACADS) is a student organization that promotes growth, leadership, and active student engagement among computer engineering students.	ACADS	2	club_applications/banners/ACADS.png	1	acads.bcp@gmail.com	t	2025-08-31 13:18:41.31085+00	4th Year
24	Junior Marketing Association 	2025-08-29 03:57:06.997689+00	1	An academic organization developing marketing skills, professionalism, and social responsibility through events, seminars, competitions, and community engagement.	JMA	2	club_applications/banners/JMA.png	1	bcpjuniormarketingassociation@gmail.com	t	2025-08-31 13:18:45.738627+00	4th Year
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	landing_page	users
8	clubs	clubs
9	clubs	clubapplication
10	clubs	memberapplication
11	clubs	memberships
12	clubs	branch
13	clubs	budgetrequest
14	clubs	event
15	clubs	achievement
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2025-08-23 05:17:48.60307+00
2	auth	0001_initial	2025-08-23 05:17:54.643083+00
3	admin	0001_initial	2025-08-23 05:17:56.105901+00
4	admin	0002_logentry_remove_auto_add	2025-08-23 05:17:56.287023+00
5	admin	0003_logentry_add_action_flag_choices	2025-08-23 05:17:56.901683+00
6	contenttypes	0002_remove_content_type_name	2025-08-23 05:17:58.004689+00
7	auth	0002_alter_permission_name_max_length	2025-08-23 05:17:58.842158+00
8	auth	0003_alter_user_email_max_length	2025-08-23 05:17:59.559022+00
9	auth	0004_alter_user_username_opts	2025-08-23 05:17:59.990989+00
10	auth	0005_alter_user_last_login_null	2025-08-23 05:18:01.014391+00
11	auth	0006_require_contenttypes_0002	2025-08-23 05:18:01.403419+00
12	auth	0007_alter_validators_add_error_messages	2025-08-23 05:18:02.035696+00
13	auth	0008_alter_user_username_max_length	2025-08-23 05:18:03.040778+00
14	auth	0009_alter_user_last_name_max_length	2025-08-23 05:18:03.859601+00
15	auth	0010_alter_group_name_max_length	2025-08-23 05:18:04.679152+00
16	auth	0011_update_proxy_permissions	2025-08-23 05:18:05.094643+00
17	auth	0012_alter_user_first_name_max_length	2025-08-23 05:18:06.010242+00
18	landing_page	0001_initial	2025-08-23 05:18:08.300906+00
19	landing_page	0002_alter_memberships_table	2025-08-23 05:18:08.754242+00
20	landing_page	0003_clubapplication	2025-08-23 05:18:09.896937+00
21	landing_page	0004_memberapplication	2025-08-23 05:18:11.335439+00
22	landing_page	0005_alter_memberapplication_student_id_card	2025-08-23 05:18:11.495635+00
23	landing_page	0006_alter_clubapplication_options_and_more	2025-08-23 05:18:12.257647+00
24	landing_page	0007_alter_clubapplication_club_name	2025-08-23 05:18:13.024886+00
25	landing_page	0008_alter_memberapplication_options_and_more	2025-08-23 05:18:13.637795+00
26	landing_page	0009_remove_memberapplication_club_and_more	2025-08-23 05:18:17.889005+00
27	landing_page	0010_users	2025-08-23 05:18:18.914057+00
28	clubs	0001_initial	2025-08-23 05:18:22.16328+00
29	clubs	0002_clubapplication_location_alter_clubs_table	2025-08-23 05:18:23.225746+00
30	clubs	0003_clubs_campus	2025-08-23 05:18:24.027273+00
31	clubs	0004_branch_remove_clubs_campus_clubs_location_and_more	2025-08-23 05:18:28.424376+00
32	clubs	0005_clubapplication_banner	2025-08-23 05:18:28.887519+00
33	clubs	0006_clubs_description	2025-08-23 05:18:29.573719+00
34	clubs	0007_alter_clubapplication_submitted_by_and_more	2025-08-23 05:18:32.319989+00
35	landing_page	0011_delete_students	2025-08-23 05:18:32.93315+00
36	sessions	0001_initial	2025-08-23 05:18:33.989829+00
37	landing_page	0012_alter_users_role	2025-08-23 10:31:48.196082+00
38	landing_page	0013_alter_users_role	2025-08-23 10:51:21.82157+00
39	clubs	0008_clubapplication_acronym_clubapplication_adviser_and_more	2025-08-24 00:52:32.126125+00
40	clubs	0009_alter_clubs_acronym	2025-08-29 03:20:56.186644+00
41	clubs	0010_alter_clubapplication_acronym	2025-08-29 03:22:14.7723+00
42	clubs	0011_budgetrequest_event	2025-08-30 03:52:17.857893+00
43	clubs	0012_alter_budgetrequest_details_and_more	2025-08-31 07:50:25.786474+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
7yiftfw1eeq2bzvlvjtiq3rb2ynhaggc	.eJyrVspNzU1KLYrPyU9PT02Jz8xTsiopKk3VgYlnpihZGcJ5eYm5qUpWSiWpxSXxxSWlKal5JUq1AFcWGME:1upgzC:Ap-iZvX8zvWT5-BFRfK1WkfmwIYhyA3aAgEoMmp83JA	2025-09-06 05:40:18.53409+00
7iv8sj3nma6x1v02nsgg5nxngd1djpgf	.eJyrVspNzU1KLYrPyU9PT02Jz8xTsiopKk3VgYlnpihZGcF5eYm5qUpWSiWpxSXxiSllmcWpRUq1AFZUGKk:1upm0o:2rSwqXoluuLYX8kgGFnuV3rULhoB43a6XaLV87Cdo0c	2025-09-06 11:02:18.925436+00
4jnwjsg13emgd0euxzdacl8sx1aossov	.eJyrVspNzU1KLYrPyU9PT02Jz8xTsiopKk3VgYlnpihZGcN5eYm5qUpWSiWpxSXx-WlpmcmpRUq1AFZBGJo:1upmD8:MEVRGAuSVVKiUXka3Cd7KrirW-Ou1t7B4qqtaplFWpI	2025-09-06 11:15:02.234995+00
6imip7bk3r04f3pf2nhdil9cv5xemgdf	.eJyrVspNzU1KLYrPyU9PT02Jz8xTsiopKk3VgYlnpihZGcF5eYm5qUpWSiWpxSXxiSllmcWpRUo6Ssk5pUlghaa1AJSQHFo:1usiB1:u8WcksrxKFAhBfhI4lsT9-s3fxJLbdY84qxC3PBgdRY	2025-09-14 13:32:59.475232+00
w5p0lm4g5s0y0kuf6pwz8onbtf0qb9ij	.eJyrVspNzU1KLYrPyU9PT02Jz8xTsiopKk3VgYlnpihZGcJ5eYm5qUpWSiWpxSXxxSWlKal5JUq1AFcWGME:1uq6jt:WqZbHmHgzeUfv_imRAI1n3VHqdXfo4xF1lca-N-1ZSU	2025-09-07 09:10:13.775217+00
vkzk8gdw9fnaly041ws5smq6vtz8uilg	.eJyrVspNzU1KLYrPyU9PT02Jz8xTsiopKk3VgYlnpihZGcJ5eYm5qUpWSiWpxSXxxSWlKal5JUq1AFcWGME:1uqRuY:ccsZJOoGiBtKoSmtOV8ipbfiQ1aIj0iMIQRrmUzYVsU	2025-09-08 07:46:38.152694+00
aydr538e7r9ioe9m7qmgfrz8iag0pl66	.eJyrVspNzU1KLYrPyU9PT02Jz8xTsiopKk3VgYlnpihZGcF5eYm5qUpWSiWpxSXxiSllmcWpRUo6Ssk5pUlghZa1AJSYHF4:1usifO:bWJBpshPu2J1ZPGTRYYwS3UuD9kV2CrXd81VXFCiYGQ	2025-09-14 14:04:22.059719+00
6s3vmcewmr4ymib48wu67xqxcdvh8w9p	.eJyrVspNzU1KLYrPyU9PT02Jz8xTsiopKk3VgYlnpihZGcF5eYm5qUpWSiWpxSXxiSllmcWpRUq1AFZUGKk:1usik3:HM_1PIZK_gfl6Z3C83sWzeKPw0u_fa84vHDZ9Bb6Eco	2025-09-14 14:09:11.392184+00
pqqw0q5z29ni8t2jety00yatnnlm4jow	.eJyrVspNzU1KLYrPyU9PT02Jz8xTsiopKk3VgYlnpihZGcF5eYm5qUpWSiWpxSXxiSllmcWpRUo6Ssk5pUlghaa1AJSQHFo:1usizz:CYuGRZYsNrV4mdtki7FvQXFAm5MNomceveQQKkfeMvs	2025-09-14 14:25:39.821824+00
hryda5ljfw1oq4jl32cv8vj07ltnxyev	.eJyrVspNzU1KLYrPyU9PT02Jz8xTsiopKk3VgYlnpihZGcJ5eYm5qUpWSiWpxSXxxSWlKal5JUo6Ssk5pUlghSa1AJZwHHE:1usj3C:C4Dn8XIU5ScF6CPLB5DUJI-URWZEKMXS1cpQ6PkCFW0	2025-09-14 14:28:58.814656+00
\.


--
-- Data for Name: event; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.event (id, name, description, start_date, end_date, club_id) FROM stdin;
\.


--
-- Data for Name: member_application; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.member_application (id, medical_form, certificate_of_recognition, student_id_card, date_submitted, club_id, student_id) FROM stdin;
\.


--
-- Data for Name: memberships; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.memberships (id, date_joined, is_officer, club_id, student_id) FROM stdin;
\.


--
-- Data for Name: school_branch; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.school_branch (id, branch_name) FROM stdin;
1	Main Campus
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (id, acc_no, password, name, role) FROM stdin;
1	0000	student	test_student	0
3	0001	officer	test_officer	1
2	0002	adviser	test_adviser	2
4	0003	activitycoordinator	activity coordinator	3
5	0004	admin	test_admin	4
\.


--
-- Name: achievement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.achievement_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 60, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: budget_requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.budget_requests_id_seq', 1, false);


--
-- Name: club_application_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.club_application_id_seq', 1, true);


--
-- Name: clubs_clubs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.clubs_clubs_id_seq', 26, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 43, true);


--
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.events_id_seq', 1, false);


--
-- Name: member_application_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.member_application_id_seq', 1, false);


--
-- Name: memberships_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.memberships_id_seq', 1, false);


--
-- Name: school_branch_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.school_branch_id_seq', 1, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 7, true);


--
-- Name: achievement achievement_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.achievement
    ADD CONSTRAINT achievement_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: budget_request budget_requests_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.budget_request
    ADD CONSTRAINT budget_requests_pkey PRIMARY KEY (id);


--
-- Name: club_application club_application_acronym_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.club_application
    ADD CONSTRAINT club_application_acronym_key UNIQUE (acronym);


--
-- Name: club_application club_application_club_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.club_application
    ADD CONSTRAINT club_application_club_name_key UNIQUE (club_name);


--
-- Name: club_application club_application_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.club_application
    ADD CONSTRAINT club_application_pkey PRIMARY KEY (id);


--
-- Name: clubs clubs_acronym_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.clubs
    ADD CONSTRAINT clubs_acronym_key UNIQUE (acronym);


--
-- Name: clubs clubs_club_name_f15f2a92_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.clubs
    ADD CONSTRAINT clubs_club_name_f15f2a92_uniq UNIQUE (club_name);


--
-- Name: clubs clubs_clubs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.clubs
    ADD CONSTRAINT clubs_clubs_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: event events_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- Name: member_application member_application_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.member_application
    ADD CONSTRAINT member_application_pkey PRIMARY KEY (id);


--
-- Name: memberships memberships_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.memberships
    ADD CONSTRAINT memberships_pkey PRIMARY KEY (id);


--
-- Name: school_branch school_branch_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.school_branch
    ADD CONSTRAINT school_branch_pkey PRIMARY KEY (id);


--
-- Name: memberships unique_membership; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.memberships
    ADD CONSTRAINT unique_membership UNIQUE (student_id, club_id);


--
-- Name: users users_acc_no_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_acc_no_key UNIQUE (acc_no);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: achievement_club_id_5573f7a6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX achievement_club_id_5573f7a6 ON public.achievement USING btree (club_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: budget_requests_club_id_0e827e6f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX budget_requests_club_id_0e827e6f ON public.budget_request USING btree (club_id);


--
-- Name: club_application_acronym_11f8eeae_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX club_application_acronym_11f8eeae_like ON public.club_application USING btree (acronym varchar_pattern_ops);


--
-- Name: club_application_adviser_id_6740a8dc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX club_application_adviser_id_6740a8dc ON public.club_application USING btree (adviser_id);


--
-- Name: club_application_club_name_ac9cae06_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX club_application_club_name_ac9cae06_like ON public.club_application USING btree (club_name varchar_pattern_ops);


--
-- Name: club_application_location_id_e9f5fd4a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX club_application_location_id_e9f5fd4a ON public.club_application USING btree (location_id);


--
-- Name: club_application_submitted_by_id_e93f892e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX club_application_submitted_by_id_e93f892e ON public.club_application USING btree (submitted_by_id);


--
-- Name: clubs_acronym_d3a8cb64_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX clubs_acronym_d3a8cb64_like ON public.clubs USING btree (acronym varchar_pattern_ops);


--
-- Name: clubs_adviser_id_c523bbd9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX clubs_adviser_id_c523bbd9 ON public.clubs USING btree (adviser_id);


--
-- Name: clubs_chairperson_id_45ead6d3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX clubs_chairperson_id_45ead6d3 ON public.clubs USING btree (chairperson_id);


--
-- Name: clubs_club_name_f15f2a92_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX clubs_club_name_f15f2a92_like ON public.clubs USING btree (club_name varchar_pattern_ops);


--
-- Name: clubs_location_id_c6daedcf; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX clubs_location_id_c6daedcf ON public.clubs USING btree (location_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: events_club_id_95a77c27; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX events_club_id_95a77c27 ON public.event USING btree (club_id);


--
-- Name: member_application_club_id_6eeb5a4c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX member_application_club_id_6eeb5a4c ON public.member_application USING btree (club_id);


--
-- Name: member_application_student_id_128aa47d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX member_application_student_id_128aa47d ON public.member_application USING btree (student_id);


--
-- Name: memberships_club_id_afa12c8a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX memberships_club_id_afa12c8a ON public.memberships USING btree (club_id);


--
-- Name: memberships_student_id_313d85d2; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX memberships_student_id_313d85d2 ON public.memberships USING btree (student_id);


--
-- Name: users_acc_no_55175e63_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX users_acc_no_55175e63_like ON public.users USING btree (acc_no varchar_pattern_ops);


--
-- Name: achievement achievement_club_id_5573f7a6_fk_clubs_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.achievement
    ADD CONSTRAINT achievement_club_id_5573f7a6_fk_clubs_id FOREIGN KEY (club_id) REFERENCES public.clubs(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: budget_request budget_requests_club_id_0e827e6f_fk_clubs_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.budget_request
    ADD CONSTRAINT budget_requests_club_id_0e827e6f_fk_clubs_id FOREIGN KEY (club_id) REFERENCES public.clubs(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: club_application club_application_adviser_id_6740a8dc_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.club_application
    ADD CONSTRAINT club_application_adviser_id_6740a8dc_fk_users_id FOREIGN KEY (adviser_id) REFERENCES public.users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: club_application club_application_location_id_e9f5fd4a_fk_school_branch_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.club_application
    ADD CONSTRAINT club_application_location_id_e9f5fd4a_fk_school_branch_id FOREIGN KEY (location_id) REFERENCES public.school_branch(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: club_application club_application_submitted_by_id_e93f892e_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.club_application
    ADD CONSTRAINT club_application_submitted_by_id_e93f892e_fk_users_id FOREIGN KEY (submitted_by_id) REFERENCES public.users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: clubs clubs_adviser_id_c523bbd9_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.clubs
    ADD CONSTRAINT clubs_adviser_id_c523bbd9_fk_users_id FOREIGN KEY (adviser_id) REFERENCES public.users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: clubs clubs_chairperson_id_45ead6d3_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.clubs
    ADD CONSTRAINT clubs_chairperson_id_45ead6d3_fk_users_id FOREIGN KEY (chairperson_id) REFERENCES public.users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: clubs clubs_location_id_c6daedcf_fk_school_branch_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.clubs
    ADD CONSTRAINT clubs_location_id_c6daedcf_fk_school_branch_id FOREIGN KEY (location_id) REFERENCES public.school_branch(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: event events_club_id_95a77c27_fk_clubs_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT events_club_id_95a77c27_fk_clubs_id FOREIGN KEY (club_id) REFERENCES public.clubs(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: member_application member_application_club_id_6eeb5a4c_fk_clubs_clubs_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.member_application
    ADD CONSTRAINT member_application_club_id_6eeb5a4c_fk_clubs_clubs_id FOREIGN KEY (club_id) REFERENCES public.clubs(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: member_application member_application_student_id_128aa47d_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.member_application
    ADD CONSTRAINT member_application_student_id_128aa47d_fk_users_id FOREIGN KEY (student_id) REFERENCES public.users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: memberships memberships_club_id_afa12c8a_fk_clubs_clubs_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.memberships
    ADD CONSTRAINT memberships_club_id_afa12c8a_fk_clubs_clubs_id FOREIGN KEY (club_id) REFERENCES public.clubs(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: memberships memberships_student_id_313d85d2_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.memberships
    ADD CONSTRAINT memberships_student_id_313d85d2_fk_users_id FOREIGN KEY (student_id) REFERENCES public.users(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

\unrestrict Je3xxBNqTlveHTZaF3rIJgbOLYMh98Bov5uqLXiXqhXAaehsPdVYhuLrD6tZMCP

