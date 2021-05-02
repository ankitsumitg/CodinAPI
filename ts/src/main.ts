import { User, userResult, Options, Clash } from "./types";
import fetch, { Response } from "node-fetch";
import { endpoints } from "./endpoints";

export class CodinClient {
	cookies?: string;
	userId?: number;
	user?: User;

	constructor(options: Options) {
		if (options && options.Email && options.Password) {
			this.Login(options.Email, options.Password, options.LoadUser || true);
		}
	}
	async Login(email: string, password: string, loadUser: boolean = true) {
		let parsedResponse;
		try {
			let response = await fetch(endpoints.login, {
				method: "POST",
				body: JSON.stringify([email, password, true]),
			});
			parsedResponse = await response.json();
			this.cookies = this.parseCookies(response);
		} catch (err) {
			return err;
		}

		this.userId = parsedResponse.userId;

		if (loadUser) {
			let user = await this.GetUserByHandle(
				parsedResponse.codinGamer.publicHandle
			);
			if (user.valid) {
				this.user = user.result;
			} else {
				return { valid: false, error: new Error("Unknown Error!") };
			}
		}
	}

	async GetUserByHandle(handle: string): Promise<userResult> {
		try {
			const User = await (
				await fetch(endpoints.getUserWithHandle, {
					method: "POST",
					body: JSON.stringify([handle]),
				})
			).json();
			if (!User.codingamer) {
				return { valid: false, error: new Error("User not found") };
			}
			return { result: User.codingamer, valid: true };
		} catch (err) {
			return { valid: false, error: err };
		}
	}
	async CreateClash(
		Modes?: string[]
	): Promise<{
		result?: Clash | undefined;
		valid: boolean;
		error?: Error | undefined;
	}> {
		if (!this.userId) {
			return {
				valid: false,
				error: new Error("You must be logged in to create clashes"),
			};
		}

		try {
			const Results = await fetch(endpoints.createClash, {
				method: "POST",
				body: JSON.stringify([
					this.userId,
					{ SHORT: true },
					[],
					Modes || ["FASTEST", "SHORTEST", "REVERSE"],
				]),
				headers: {
					cookie: this.cookies || "",
				},
			});
			return { result: await Results.json(), valid: true };
		} catch (err) {
			return { valid: false, error: err };
		}
	}

	async StartClash(handle: string) {
		try {
			await fetch(endpoints.startClash, {
				method: "POST",
				body: JSON.stringify([this.userId, handle]),
				headers: {
					cookie: this.cookies || "",
				},
			});
			return { valid: true };
		} catch (err) {
			return { valid: false, error: err };
		}
	}

	async getClashInfo(handle: string) {
		try {
			const Results = await fetch(endpoints.getClash, {
				method: "POST",
				body: JSON.stringify([handle]),
			});
			return { result: await Results.json(), valid: true };
		} catch (err) {
			return { valid: false, error: err };
		}
	}
	async getPending() {
		try {
			const Res = await fetch(endpoints.getPendingClashes, {
				method: "POST",
				body: JSON.stringify([]),
			});
			return Res.json();
		} catch (err) {
			return { valid: false, error: err };
		}
	}

	parseCookies(res: Response) {
		let rawHeaders = res.headers.raw();
		let cookie = rawHeaders["set-cookie"];
		return cookie
			.map((entry) => {
				let parts = entry.split(";");
				let cookiePart = parts[0];
				return cookiePart;
			})
			.join(";");
	}
}
