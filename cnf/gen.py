import click
import os
from random import sample, randint, choice
from hashlib import md5


@click.command()
@click.option('--num-vars', '-v', type=int, required=True,
              help='Number of variables')
@click.option('--num-clauses', '-c', type=int, required=True,
              help='Number of clauses')
@click.option('--len-limit', '-l', type=int, required=True,
              help='Clause length limit')
@click.option('--len-fixed', '-f', is_flag=True,
              help='Clause lengths are fixed')
@click.option('--print-only', '-p', is_flag=True,
              help='Prints to stdout instead of writing to file')
@click.option('--target-dir', '-o', default=None,
              help='Target directory for output file (omit for ".")')
def gen(num_vars, num_clauses, len_limit, len_fixed, print_only, target_dir):
    if len_limit > num_vars:
        raise RuntimeError('Invalid clause length limit.')
    clauses = []
    while len(clauses) < num_clauses:
        clause_len = len_limit if len_fixed else randint(1, len_limit)
        clause = [
            choice((-1, 1)) * i
            for i in sorted(sample(
                range(1, num_vars + 1),
                clause_len
            ))
        ]
        if clause not in clauses:
            clauses.append(clause)
    cnf = '{}\n{}\n'.format(
        'p cnf {} {}'.format(num_vars, num_clauses),
        '\n'.join(
            [' '.join([str(v) for v in c + [0]])
             for c in clauses]
        )
    )
    fp = md5(cnf.encode('utf-8')).hexdigest()
    if print_only:
        print(cnf)
    else:
        target_file = os.path.join(
            '.' if not target_dir else target_dir,
            'cnf_var={}_clause={}_len={}_fixed={}_md5={}.cnf'.format(
                num_vars,
                num_clauses,
                len_limit,
                len_fixed,
                fp
            )
        )
        with open(target_file, 'w') as f:
            f.write(cnf)
