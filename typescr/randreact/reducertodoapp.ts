function reducer(todos: any, action: any) {
	function newTodo(name: string) {
		return {id: Date.now(), name: name, complete: false}
	}

	switch (action.type) {
		case 'add':
			return [...todos, newTodo(action.payload.name)]
		case 'toggle':
			return todos.map((todo: any) => todo.id === action.payload.id ? 
				{ ...todo, complete: !todo.complete } : todo )
		case 'delete':
			return todos.filter((todo: any) => todo.id !== action.payload.id)
		default:
			return todos;
	}
}

function Reducer(): JSX.Element {
	const [todos, dispatch] = useReducer(reducer, [])
	const [name, setName] = useState('')

	function submitHand(e: any) {
		e.preventDefault()
		setName('')

		dispatch({type: 'add', payload: {name: name}})
	}

	return <div>
		<form action="" onSubmit={submitHand}>
			<input type="text" value={name} onChange={e => setName(e.target.value)} />
		</form>

		{todos.map((todo: any) => <Todo key={todo.id} todo={todo} dispatch={dispatch}/>)}
	</div>
}

function Todo({ todo, dispatch }: any): JSX.Element {
	return <div>
		<span style={{color: todo.complete ? '#AAA' : '#000'}}>{todo.name}</span>
		<button onClick={() => dispatch({ type: 'toggle', payload: { id: todo.id } })}>Toggle</button>
		<button onClick={() => dispatch({ type: 'delete', payload: { id: todo.id } })}>Delete</button>
	</div>
}
