<script lang="ts">
	import { writable } from 'svelte/store';

	import { Shell } from '$lib/components/layout/shell';
	import SideNav from './SideNav.svelte';

	import { CircleUserRound, Dna, LogOut, MessagesSquare, UsersRound, Zap } from 'lucide-svelte';
	import type { ComponentType } from 'svelte';
	import { type Icon } from 'lucide-svelte';
	import { setContext } from '$lib/utils';

	export let data;

	const subscriptionStore = writable({
		sub: data.stripeSub,
		tier: data.userTier,
		paymentMethod: data.paymentMethod
	});

	setContext('subscriptionStore', subscriptionStore);

	$: subscribed = Boolean($subscriptionStore.sub);

	let navigations: {
		name: string;
		items: {
			name: string;
			href: string;
			icon: ComponentType<Icon>;
			current: boolean;
			pendingCount?: number;
		}[];
	}[] = [
		{
			name: '',
			items: [
				{
					name: 'Auto-build',
					href: '/app/auto-build',
					icon: Zap,
					current: false
				},
				{
					name: 'Sessions',
					href: '/app/sessions',
					icon: MessagesSquare,
					current: false
				}
			]
		},
		{
			name: '',
			items: [
				{
					name: 'Crews',
					href: '/app/crews',
					icon: UsersRound,
					current: false
				},
				{ name: 'Agents', href: '/app/agents', icon: Dna, current: false }
			]
		},
		{
			name: '',
			items: [
				{
					name: 'Account',
					href: '/app/account',
					icon: CircleUserRound,
					current: false
				}
			]
		}
	];
	let bottomNavigation = [{ name: 'Logout', href: 'logout', icon: LogOut, current: false }];
</script>

<Shell class="h-screen">
	<svelte:fragment slot="sidebarLeft">
		{#key subscribed}
			<SideNav user={data.user} {navigations} {bottomNavigation} {subscribed} />
		{/key}
	</svelte:fragment>

	<slot />
</Shell>
