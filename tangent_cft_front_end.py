import argparse

from Embedding_Preprocessing.encoder_tuple_level import TupleTokenizationMode
from tangent_cft_back_end import TangentCFTBackEnd


def main():
    parser = argparse.ArgumentParser(description='Given the configuration file for training Tangent_CFT model.'
                                                 'This function train the model and then does the retrieval task on'
                                                 'NTCIR-12 formula retrieval task.')

    parser.add_argument('--t', type=bool, help="Value True for training a new model and False for loading a model",
                        default=True)
    parser.add_argument('--r', type=bool, help="Value True to do the retrieval on NTCIR12 dataset",
                        default=True)
    parser.add_argument('-ds', type=str, help="File path of training data. If using NTCIR12 dataset, "
                                              "it should be MathTagArticles directory. If using the MSE dataset, it"
                                              "should be csv file of formula", required=True)
    parser.add_argument('-cid', metavar='cid', type=int, help='Configuration file.', required=True)
    parser.add_argument('--wiki', type=bool, help="Determines if the dataset is wiki or not.", default=True)
    parser.add_argument('--slt', type=bool, help="Determines to use slt (True) or opt(False)", default=True)
    parser.add_argument('-em', type=str, help="File path for encoder map.", required=True)
    parser.add_argument('--mp', type=str, help="Model file path.", default=None)
    parser.add_argument('--qd', type=str, help="NTCIR12 query directory.", default=None)
    parser.add_argument('--rf', type=str, help="Retrieval result file path.", default="ret_res")
    parser.add_argument('--ri', type=int, help="Run Id for Retrieval.", default=1)
    parser.add_argument('--frp', type=bool, help="Determines to ignore full relative path", default=True)
    parser.add_argument('--ta', type=bool, help="Determines to tokenize all", default=False)
    parser.add_argument('--tn', type=bool, help="Determines to tokenize numbers", default=True)
    parser.add_argument('--et', help='Embedding type; 1:Value, 2:Type, 3:Type and Value separated and'
                                     ' 4: Type and Value Not Separated', choices=range(1, 5),
                        default=3, type=int)

    args = vars(parser.parse_args())

    do_retrieval = args['r']
    if do_retrieval:
        encoder_file_path = args['em']
        map_file_path = f"Embedding_Preprocessing/{str(encoder_file_path)}"
        embedding_type = TupleTokenizationMode(args['et'])
        config_id = args['cid']
        config_file_path = f"Configuration/config/config_{str(config_id)}"

        dataset_file_path = args['ds']
        is_wiki = args['wiki']
        read_slt = args['slt']
        queries_directory_path = args['qd']
        system = TangentCFTBackEnd(config_file=config_file_path, path_data_set=dataset_file_path, is_wiki=is_wiki,
                                   read_slt=read_slt, queries_directory_path=queries_directory_path)
        train_model = args['t']
        model_file_path = args['mp']
        ignore_full_relative_path = args['frp']
        tokenize_all = args['ta']
        tokenize_number = args['tn']
        dictionary_formula_tuples_collection = (
            system.train_model(
                map_file_path=map_file_path,
                model_file_path=model_file_path,
                embedding_type=embedding_type,
                ignore_full_relative_path=ignore_full_relative_path,
                tokenize_all=tokenize_all,
                tokenize_number=tokenize_number,
            )
            if train_model
            else system.load_model(
                map_file_path=map_file_path,
                model_file_path=model_file_path,
                embedding_type=embedding_type,
                ignore_full_relative_path=ignore_full_relative_path,
                tokenize_all=tokenize_all,
                tokenize_number=tokenize_number,
            )
        )
        retrieval_result = system.retrieval(dictionary_formula_tuples_collection,
                                            embedding_type, ignore_full_relative_path, tokenize_all,
                                            tokenize_number
                                            )
        res_file = args['rf']
        run_id = args['ri']
        system.create_result_file(
            retrieval_result, f"Retrieval_Results/{res_file}", run_id
        )


if __name__ == "__main__":
    main()
