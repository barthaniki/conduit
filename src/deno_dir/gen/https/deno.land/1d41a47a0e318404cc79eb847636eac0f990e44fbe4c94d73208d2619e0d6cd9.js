import { deferred } from "../deps.ts";
export class DeferredStack {
    #array;
    #creator;
    #max_size;
    #queue;
    #size;
    constructor(max, ls, creator) {
        this.#array = ls ? [...ls] : [];
        this.#creator = creator;
        this.#max_size = max || 10;
        this.#queue = [];
        this.#size = this.#array.length;
    }
    get available() {
        return this.#array.length;
    }
    async pop() {
        if (this.#array.length > 0) {
            return this.#array.pop();
        }
        else if (this.#size < this.#max_size && this.#creator) {
            this.#size++;
            return await this.#creator();
        }
        const d = deferred();
        this.#queue.push(d);
        await d;
        return this.#array.pop();
    }
    push(value) {
        this.#array.push(value);
        if (this.#queue.length > 0) {
            const d = this.#queue.shift();
            d.resolve();
        }
    }
    get size() {
        return this.#size;
    }
}
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZGVmZXJyZWQuanMiLCJzb3VyY2VSb290IjoiIiwic291cmNlcyI6WyJkZWZlcnJlZC50cyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQSxPQUFPLEVBQVksUUFBUSxFQUFFLE1BQU0sWUFBWSxDQUFDO0FBRWhELE1BQU0sT0FBTyxhQUFhO0lBQ3hCLE1BQU0sQ0FBVztJQUNqQixRQUFRLENBQW9CO0lBQzVCLFNBQVMsQ0FBUztJQUNsQixNQUFNLENBQXFCO0lBQzNCLEtBQUssQ0FBUztJQUVkLFlBQ0UsR0FBWSxFQUNaLEVBQWdCLEVBQ2hCLE9BQTBCO1FBRTFCLElBQUksQ0FBQyxNQUFNLEdBQUcsRUFBRSxDQUFDLENBQUMsQ0FBQyxDQUFDLEdBQUcsRUFBRSxDQUFDLENBQUMsQ0FBQyxDQUFDLEVBQUUsQ0FBQztRQUNoQyxJQUFJLENBQUMsUUFBUSxHQUFHLE9BQU8sQ0FBQztRQUN4QixJQUFJLENBQUMsU0FBUyxHQUFHLEdBQUcsSUFBSSxFQUFFLENBQUM7UUFDM0IsSUFBSSxDQUFDLE1BQU0sR0FBRyxFQUFFLENBQUM7UUFDakIsSUFBSSxDQUFDLEtBQUssR0FBRyxJQUFJLENBQUMsTUFBTSxDQUFDLE1BQU0sQ0FBQztJQUNsQyxDQUFDO0lBRUQsSUFBSSxTQUFTO1FBQ1gsT0FBTyxJQUFJLENBQUMsTUFBTSxDQUFDLE1BQU0sQ0FBQztJQUM1QixDQUFDO0lBRUQsS0FBSyxDQUFDLEdBQUc7UUFDUCxJQUFJLElBQUksQ0FBQyxNQUFNLENBQUMsTUFBTSxHQUFHLENBQUMsRUFBRTtZQUMxQixPQUFPLElBQUksQ0FBQyxNQUFNLENBQUMsR0FBRyxFQUFHLENBQUM7U0FDM0I7YUFBTSxJQUFJLElBQUksQ0FBQyxLQUFLLEdBQUcsSUFBSSxDQUFDLFNBQVMsSUFBSSxJQUFJLENBQUMsUUFBUSxFQUFFO1lBQ3ZELElBQUksQ0FBQyxLQUFLLEVBQUUsQ0FBQztZQUNiLE9BQU8sTUFBTSxJQUFJLENBQUMsUUFBUSxFQUFFLENBQUM7U0FDOUI7UUFDRCxNQUFNLENBQUMsR0FBRyxRQUFRLEVBQUssQ0FBQztRQUN4QixJQUFJLENBQUMsTUFBTSxDQUFDLElBQUksQ0FBQyxDQUFDLENBQUMsQ0FBQztRQUNwQixNQUFNLENBQUMsQ0FBQztRQUNSLE9BQU8sSUFBSSxDQUFDLE1BQU0sQ0FBQyxHQUFHLEVBQUcsQ0FBQztJQUM1QixDQUFDO0lBRUQsSUFBSSxDQUFDLEtBQVE7UUFDWCxJQUFJLENBQUMsTUFBTSxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsQ0FBQztRQUN4QixJQUFJLElBQUksQ0FBQyxNQUFNLENBQUMsTUFBTSxHQUFHLENBQUMsRUFBRTtZQUMxQixNQUFNLENBQUMsR0FBRyxJQUFJLENBQUMsTUFBTSxDQUFDLEtBQUssRUFBRyxDQUFDO1lBQy9CLENBQUMsQ0FBQyxPQUFPLEVBQUUsQ0FBQztTQUNiO0lBQ0gsQ0FBQztJQUVELElBQUksSUFBSTtRQUNOLE9BQU8sSUFBSSxDQUFDLEtBQUssQ0FBQztJQUNwQixDQUFDO0NBQ0YifQ==