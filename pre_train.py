from prompt_graph.pretrain import Edgepred_GPPT, Edgepred_Gprompt, GraphCL, SimGRACE, PrePrompt, DGI
from prompt_graph.utils import seed_everything
from prompt_graph.utils import mkdir, get_args


args = get_args()
seed_everything(args.seed)
mkdir('./pre_trained_gnn/')
args.task = 'DGI'
if args.task == 'SimGRACE':
    pt = SimGRACE(dataset_name = args.dataset_name, gnn_type = args.gnn_type, hid_dim = args.hid_dim, gln = args.num_layer, num_epoch=args.epochs, device=args.device)
if args.task == 'GraphCL':
    pt = GraphCL(dataset_name = args.dataset_name, gnn_type = args.gnn_type, hid_dim = args.hid_dim, gln = args.num_layer, num_epoch=args.epochs, device=args.device)
if args.task == 'Edgepred_GPPT':
    pt = Edgepred_GPPT(dataset_name = args.dataset_name, gnn_type = args.gnn_type, hid_dim = args.hid_dim, gln = args.num_layer, num_epoch=args.epochs, device=args.device)
if args.task == 'Edgepred_Gprompt':
    pt = Edgepred_Gprompt(dataset_name = args.dataset_name, gnn_type = args.gnn_type, hid_dim = args.hid_dim, gln = args.num_layer, num_epoch=args.epochs, device=args.device)
if args.task == 'DGI':
    pt = DGI(dataset_name = args.dataset_name, gnn_type = args.gnn_type, hid_dim = args.hid_dim, gln = args.num_layer, num_epoch=args.epochs, device=args.device)
if args.task == 'MultiGprompt':
    nonlinearity = 'prelu'
    pt = PrePrompt(args.dataset_name, args.hid_dim, nonlinearity, 0.9, 0.9, 0.1, 0.001, 2, 0.3)
pt.pretrain()

