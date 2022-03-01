function Stopwatch(): JSX.Element {
	const [time, setTime] = useState<number>(0)
  	const [running, setRunning] = useState<boolean>(false)

	useEffect((): (() => void) | void => {
		if (!running) return

		const timerInterval: NodeJS.Timer = setInterval((): void => {
			setTime((prev) => prev + 10)
		}, 10)
		return (): void => clearInterval(timerInterval)
	}, [running])

	const [hr, min, sec, ltsec] = [
		'N/A', 
		('0' + Math.floor((time / 60000) % 60)).slice(-2), 
		('0' + Math.floor((time / 1000) % 60)).slice(-2), 
		('0' + ((time / 10) % 100)).slice(-2)
	]

	return <div>
		<h1>time: {`${hr} : ${min} : ${sec} : ${ltsec}`}</h1>

		{/* <button onClick={() => setRunning((prev: boolean): boolean => !prev)}>{running ? 'Stop run' : 'Start run'}</button> */}
		<button onClick={() => setRunning(true)}>start</button>
		<button onClick={() => setRunning(false)}>stop</button>
		<button onClick={() => setTime(0)}>reset</button>
	</div>
}
