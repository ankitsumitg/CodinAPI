export interface User {
	pseudo: string;
	userId: number;
	email: string;
	countryId: string;
	publicHandle: string;
	formValues: object;
	enable: boolean;
	rank: number;
	tagline: string;
	company: string;
	level: number;
	xp: number;
	category: string;
}
export interface Clash {
	nbPlayersMin: number;
	nbPlayersMax: number;
	publicHandle: string;
	clashDurationTypeId: string;
	creationTime: string;
	startTime: string;
	msBeforeStart: number;
	finished: boolean;
	started: boolean;
	publicClash: true;
	players: Player[];
}

export interface Player {
	codingamerId: number;
	duration: number;
	status: string;
}

export interface userResult {
	valid?: boolean;
	result?: User;
	error?: Error;
}
export interface Options {
	Email: string;
	Password: string;
	LoadUser: boolean;
}
