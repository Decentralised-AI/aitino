<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import api, { type schemas } from '$lib/api';
	import { goto } from '$app/navigation';

	export let data;

	let profileId = data.profileId;
	let crews = data.crews;
	let crew: schemas['Crew'] | undefined = crews[0];

	async function startNewSession(profileId: string, crewId: string, title: string) {
		const runResponse = await api
			.POST('/sessions/run', {
				body: {
					crew_id: crewId,
					profile_id: profileId,
					session_title: title
				}
			})
			.then(({ data: d, error: e }) => {
				if (e) {
					console.error(`Error running crew: ${e.detail}`);
					return null;
				}
				if (!d) {
					console.error('Failed to start session');
					return null;
				}
				return d;
			});

		if (!runResponse) {
			return;
		}

		goto(`/app/sessions/${runResponse.id}`); // Can this be done better without full page reload?
	}
</script>

{#if crew}
	<div
		class="xl:prose-md prose prose-sm prose-main mx-auto flex h-screen max-w-none flex-col items-center justify-center gap-4 px-12 text-center md:prose-base 2xl:prose-lg"
	>
		<h1>It looks like you haven't started a session yet...</h1>
		<!-- TODO: Allow user to choose crew -->

		<Button on:click={() => crew && startNewSession(profileId, crew.id, 'New Session')}
			>Run Your Crew!</Button
		>
	</div>
{:else}
	<div
		class="xl:prose-md prose prose-sm prose-main mx-auto mt-auto flex h-full max-w-none flex-col items-center justify-center gap-4 px-12 text-center md:prose-base 2xl:prose-lg"
	>
		<h1>Looks like you haven't created your own crew yet...</h1>
	</div>
{/if}
